from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3, inet
from ryu.lib.packet import packet, ethernet, ipv4, udp, arp, ether_types

alert_switch_dpid = 1

beacon_ip = {
    "192.168.1.1": [1],
    "172.16.1.1": [2],
    "8.8.8.8": [3],
    "1.1.1.1": [4],
    "77.77.77.77": [1, 2, 3, 4]
}

terminal_port = {
    20: [1],
    22: [2],
    3389: [3],
    443: [4],
    7777: [1, 2, 3, 4]
}

beacon_dpid = {1: 2, 2: 3, 3: 4, 4: 5}
beacon_to_terminal_ports = {
    1: {1: 2, 2: 3, 3: 4, 4: 5},
    2: {1: 2, 2: 3, 3: 4, 4: 5},
    3: {1: 2, 2: 3, 3: 4, 4: 5},
    4: {1: 2, 2: 3, 3: 4, 4: 5}
}
alert_to_beacon_port = {1: 2, 2: 3, 3: 4, 4: 5}

class MilitaryAlertController(app_manager.RyuApp):

    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(MilitaryAlertController, self).__init__(*args, **kwargs)
        self.datapaths = {}
        print("[FEED] Controller started, ready to process coded packets")


    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        self.datapaths[datapath.id] = datapath

        parser = datapath.ofproto_parser
        ofproto = datapath.ofproto

        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER)] 
        self.install_flow(datapath=datapath, priority=0, match=match, actions=actions, idle_timeout=0)

        print(f"[FEED] Switch Connected, DPID: {datapath.id}")


    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        in_port = msg.match.get("in_port")
        pkt = packet.Packet(msg.data)

        eth = pkt.get_protocol(ethernet.ethernet)
        ip_pkt = pkt.get_protocol(ipv4.ipv4)
        udp_pkt = pkt.get_protocol(udp.udp)

        if not eth or pkt.get_protocol(arp.arp):
            return
        
        if not ip_pkt or not udp_pkt:
            return
        
        dst_ip = ip_pkt.dst
        dst_port = udp_pkt.dst_port

        if ip_pkt.src == "254.254.254.254" and ip_pkt.dst == "253.253.253.253" and udp_pkt.dst_port == 1:
            return

        if dst_ip in beacon_ip and dst_port in terminal_port:
            beacons = beacon_ip[dst_ip]
            terminals = terminal_port[dst_port]
            self.obfuscate_and_send_packet_out(datapath, msg, pkt, in_port, beacons, terminals)
        else:
            return
    

    def install_flow(self, datapath, priority, match, actions=[], idle_timeout=30, hard_timeout=0):
        parser = datapath.ofproto_parser
        ofproto = datapath.ofproto

        instructions = []

        if actions:
            instructions.append(parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions))

        mod = parser.OFPFlowMod(
            datapath=datapath,
            priority=priority,
            match=match,
            instructions=instructions,
            idle_timeout=idle_timeout,
            hard_timeout=hard_timeout
        )
        datapath.send_msg(mod)
        print(f"[FEED] Temporary flow installed on DPID {datapath.id}")


    def install_beacon_flow(self, beacon_datapath, terminal_port):
        if beacon_datapath is None:
            return
        
        parser = beacon_datapath.ofproto_parser
        ofproto = beacon_datapath.ofproto

        match = parser.OFPMatch(eth_type=ether_types.ETH_TYPE_IP, ipv4_dst="253.253.253.253", ip_proto=17, udp_dst=1)

        if terminal_port:
            for p in terminal_port:
                actions = [parser.OFPActionOutput(p)]
            
        else:
            actions = [parser.OFPActionOutput(ofproto.OFPP_FLOOD)]
        
        self.install_flow(beacon_datapath, priority=200, match=match, actions=actions, idle_timeout=30)


    def obfuscate_and_send_packet_out(self, datapath, msg, pkt, in_port, beacons, terminals):
        alert_datapath = self.datapaths.get(alert_switch_dpid, datapath)
        alert_parser = alert_datapath.ofproto_parser
        alert_ofproto = alert_datapath.ofproto
        buffer_id = msg.buffer_id
        out_in_port = alert_ofproto.OFPP_CONTROLLER
        print("[FEED] Obfuscating packet information")

        for b in beacons:
            beacon_switch_id = beacon_dpid.get(b)
            beacon_datapath = self.datapaths.get(beacon_switch_id)

            terminal_map = beacon_to_terminal_ports.get(b, {})
            terminal_ports = []

            for terminal_id in terminals:
                if terminal_id in terminal_map:
                    terminal_ports.append(terminal_map[terminal_id])
            
            if terminal_ports:
                self.install_beacon_flow(beacon_datapath, terminal_ports)
            else:
                self.install_beacon_flow(beacon_datapath, None)

        for b in beacons:
            out_port = alert_to_beacon_port.get(b, alert_ofproto.OFPP_FLOOD)
            actions = [
                alert_parser.OFPActionSetField(ipv4_src="254.254.254.254"),
                alert_parser.OFPActionSetField(ipv4_dst="253.253.253.253"),
                alert_parser.OFPActionSetField(udp_dst=1),
                alert_parser.OFPActionOutput(out_port)
            ]
            pkt_out = alert_parser.OFPPacketOut(
                datapath=alert_datapath,
                buffer_id=msg.buffer_id,
                in_port=out_in_port,
                actions=actions,
                data=msg.data
            )
            alert_datapath.send_msg(pkt_out)
            print(f"[FEED] Packet forwarded from Alert Switch... Sending to beacon {b} and port {terminal_id}")


    @set_ev_cls(ofp_event.EventOFPErrorMsg, MAIN_DISPATCHER)
    def error_msg_handler(self, ev):
        """
        Handles OpenFlow error messages from switches.
        """
        msg = ev.msg
        switch_id = ev.msg.datapath.id
        ofproto = ev.msg.datapath.ofproto
        
        if hasattr(ofproto, 'ofp_error_type_to_str'):
            type_str = ofproto.ofp_error_type_to_str(msg.type).split('(')[0]
        else:
            type_str = f"Type({msg.type})"
        
        if hasattr(ofproto, 'ofp_error_code_to_str'):
            code_str = ofproto.ofp_error_code_to_str(msg.type, msg.code).split('(')[0]
        else:
            code_str = f"Code({msg.code})"
        
        header_line = f"--- OpenFlow Error from Switch with DPID {switch_id} ---"
        
        self.logger.error(f"\n{header_line}")
        self.logger.error(f"Type: {type_str}")
        self.logger.error(f"Code: {code_str}")
        self.logger.error(f"Error code reference:")
        self.logger.error(f"  https://github.com/osrg/ryu/blob/master/ryu/ofproto/ofproto_v1_3.py")
        self.logger.error(f"  (Search for OFPET_ and {code_str})")
        self.logger.error("-" * len(header_line))
