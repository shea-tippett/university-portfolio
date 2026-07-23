from mininet_helpers import createInitialNetwork, safeMininetStartupAndExit

# ╔══════════════════════════════════════════════╗
# ║              TOPOLOGY DEFINITIONS            ║
# ╚══════════════════════════════════════════════╝
# These are the network topologies you can actually launch in Mininet.
# Copy/paste templateTopology(), rename it, and modify it to make your own.
# Then scroll to the bottom and register it in the 'topos' dictionary.

def basicExampleTopology():
    net = createInitialNetwork()

    # Add hosts with set IPs
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    h3 = net.addHost('h3', ip='192.168.1.1/24')

    # Add a switch
    s1 = net.addSwitch('s1')

    # Connect hosts to switch
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1, loss=10)  # Add 10% packet loss just for fun/testing

    # This always needs to be added, otherwise the network simulatiion won't start.
    net.start()

    # IMPORTANT: Don't run post-launch logic (e.g. ping, cmd) until net.start() has been called!
    print("\nPing between h1 and h2:")
    net.ping([h1, h2])
    print("\nPing between h1 and h3 (different subnets):")
    net.ping([h1, h3])

    safeMininetStartupAndExit(net)


def advancedExampleTopology():
    net = createInitialNetwork()

    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')

    # If you add switches with the traditional naming scheme of s1/s2/s3, it adds a 'DPID' sequentially automatically.
    # The DPID is important as it can be used to identify your switch in an SDN Program. I.e., "if DPID == 1, then do xyz"

    s1 = net.addSwitch('s1') # This will give the DPID of '1'

    # HOWEVER, unique switch names requires a bit of extra configuration. You need to manually specify the DPID yourself.

    leaf1 = net.addSwitch('leaf1', dpid='2') # We start from 2 because s1 already has the DPID of 1.
    leaf2 = net.addSwitch('leaf2', dpid='3')
    spine = net.addSwitch('spine', dpid='4')

    net.addLink(leaf1, spine)
    net.addLink(h1, leaf1)

    net.addLink(leaf2, spine)

    # This always needs to be added, otherwise the network simulatiion won't start.
    net.start()

    # You can run specific commands on a host device, as if it's a real computer.
    # Much like pings, this can only be done after net.start() has been called.

    # Example of setting a static ARP entry manually
    h1.cmd("arp -s 10.0.0.2 00:00:00:00:00:02")


    safeMininetStartupAndExit(net)


def oneSwitchThreeHost():
    net = createInitialNetwork()

    # Basic 3-host, 1-switch setup
    s1 = net.addSwitch('s1')

    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    h3 = net.addHost('h3', ip='10.0.0.3/24')


    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)

    net.start()
    safeMininetStartupAndExit(net)

def threeSwitchThreeHost():
    net = createInitialNetwork()

    # A small spine-like topology across 3 switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')

    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    h3 = net.addHost('h3', ip='10.0.0.3/24')

    net.addLink(h1, s1)
    net.addLink(s1, s2)
    net.addLink(h2, s2)
    net.addLink(s2, s3)
    net.addLink(h3, s3)

    net.start()
    safeMininetStartupAndExit(net)

def collapsedCore():
    net = createInitialNetwork()

    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    h1 = net.addHost('h1', ip='192.10.0.1')
    h2 = net.addHost('h2', ip='192.10.0.2')
    h3 = net.addHost('h3', ip='192.10.0.3')

    net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s1, h3)
    net.addLink(s2, h1)
    net.addLink(s2, h2)
    net.addLink(s2, h3)
    net.addLink(s1, s2)

    net.start()
    safeMininetStartupAndExit(net)

def mazeTopology():

    net = createInitialNetwork()

    s1 = net.addSwitch('s1')

    h1 = net.addHost('h1', ip='10.0.0.1', defaultRoute='via 10.0.0.254')

    net.addLink(s1, h1)

    net.start()

    h1.cmd('arp -s 10.0.0.254 00:00:00:00:00:02')

    safeMininetStartupAndExit(net)

def LoadBalancerTopology():
    net = createInitialNetwork()

    h1 = net.addHost('h1', ip='10.0.0.1/24')  # Host 1
    h2 = net.addHost('h2', ip='10.0.0.101/24')  # Host 2
    h3 = net.addHost('h3', ip='10.0.0.102/24')  # Host 3

    s1 = net.addSwitch('s1')

    # Add links from s1 to the three PCs
    net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s1, h3)

    net.start()

    # To simplify this week, we are not going to worry about dealing with ARP, only IP. So, we will set a static ARP Entry for 10.0.0.100.
    # This MAC Address does not exist, and it does not need to. We're just adding this so it never does an ARP Request, so we don't have to deal with it.
    h1.cmd("arp -s 10.0.0.100 10:10:f0:80:81:4b")

    safeMininetStartupAndExit(net)

def militaryAlertSystemTopology():
    net = createInitialNetwork()

    # Alert switch and beacons
    a1 = net.addSwitch('a1', dpid='1', defaultRoute='via 10.0.0.254')
    b1 = net.addSwitch('b1', dpid='2')
    b2 = net.addSwitch('b2', dpid='3')
    b3 = net.addSwitch('b3', dpid='4')
    b4 = net.addSwitch('b4', dpid='5')

    # Alert terminal
    a1t1 = net.addHost('a1t1')

    # Beacon 1 terminals
    b1t1 = net.addHost('b1t1')
    b1t2 = net.addHost('b1t2')
    b1t3 = net.addHost('b1t3')
    b1t4 = net.addHost('b1t4')

    # Beacon 2 terminals
    b2t1 = net.addHost('b2t1')
    b2t2 = net.addHost('b2t2')
    b2t3 = net.addHost('b2t3')
    b2t4 = net.addHost('b2t4')

    # Beacon 3 terminals
    b3t1 = net.addHost('b3t1')
    b3t2 = net.addHost('b3t2')
    b3t3 = net.addHost('b3t3')
    b3t4 = net.addHost('b3t4')

    # Beacon 4 terminals
    b4t1 = net.addHost('b4t1')
    b4t2 = net.addHost('b4t2')
    b4t3 = net.addHost('b4t3')
    b4t4 = net.addHost('b4t4')

    # Alert - beacon links
    net.addLink(a1, a1t1)
    net.addLink(a1, b1)
    net.addLink(a1, b2)
    net.addLink(a1, b3)
    net.addLink(a1, b4)

    # Beacon 1 - terminal links
    net.addLink(b1, b1t1)
    net.addLink(b1, b1t2)
    net.addLink(b1, b1t3)
    net.addLink(b1, b1t4)

    # Beacon 2 - terminal links
    net.addLink(b2, b2t1)
    net.addLink(b2, b2t2)
    net.addLink(b2, b2t3)
    net.addLink(b2, b2t4)

    # Beacon 3 - terminal links
    net.addLink(b3, b3t1)
    net.addLink(b3, b3t2)
    net.addLink(b3, b3t3)
    net.addLink(b3, b3t4)

    # Beacon 4 - terminal links
    net.addLink(b4, b4t1)
    net.addLink(b4, b4t2)
    net.addLink(b4, b4t3)
    net.addLink(b4, b4t4)

    net.start()

    a1t1.cmd("ip route add default via 10.0.0.254")
    a1t1.cmd('arp -s 10.0.0.254 02:aa:bb:cc:dd:ee')

    safeMininetStartupAndExit(net)


# ╔══════════════════════════════════════════════╗
# ║              TOPOLOGY REGISTRATION           ║
# ╚══════════════════════════════════════════════╝
# This dictionary lets you run your topologies from the terminal using --topo.
# It maps a name you choose (on the left) to the actual function that builds the network (on the right).
#
# For example, if you create a function like:
#   def starTopology():
# And want to launch it with:
#   sudo mn --custom ~/Documents/SDN\ Scripts/mininet_custom_helper.py --topo star
# You’d need to add this line:
#   'star': (lambda: starTopology())
#
# Left side = the name you type after --topo
# Right side = the function that sets up the network (wrapped in lambda)

topos = {
    'basicExample': (lambda: basicExampleTopology()),
    'advancedExample': (lambda: advancedExampleTopology()),
    '1Switch3Host': (lambda: oneSwitchThreeHost()),
    '3Switch3Host': (lambda: threeSwitchThreeHost()),
    'week12': (lambda: mazeTopology()),
    'week13': (lambda: LoadBalancerTopology()),
    'militaryAlertSystem': (lambda: militaryAlertSystemTopology())
    # Add your own as needed
}