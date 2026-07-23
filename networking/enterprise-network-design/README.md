# Enterprise Network Design

The purpose of this project is to create an enterprise network for a video production company situated in South Australia.

---

## Overview

This comapny has two offices: 

1. The Adelaide Office - Their main headquaters that will host 50 video production and 30 admin staff, totaling 80 staff spanning two floors, with the two staff roles split onto each floor.
    - Expansion - Over the next 5 years staff and rented floors are expeted to double, this need to be accounted for.
2. The Plympton Office - This office hosts 5 video production staff and 45 admin staff, totaling 50 staff spanning two small buildings, with 25 staff each.

---

## Current Equipment

The company has pre-purchased equipment that needs to be accounted for:

- Storage Server - Has 2x100QFSP+ NICs and is only located at Adelaide office.
- AD Server - Has 1x10G SFP+ NIC.
- Admin Workstations - Each have 1Gbps NICs
- Video Production Workstations - Each have 10G BASE-T NICs and use ethernet cables.
- Security Cameras - Only used at Adelaide office and store data on Storage Server.
- WAP - 2x in every room.

---

## How Open

1. Download `video_production_company(logical_diagram).drawio`, `video_production_company(physical_diagram).drawio` and `ip_addressing_scheme_and_equipment.xlsx`
2. Use Excel to open and view `ip_addressing_scheme_and_equipment.xlsx`
3. Navigate to https://www.drawio.com/
4. Click `Start Diagramming`
5. Click `File`, `Open From`, `Device...`
6. Open either `video_production_company(logical_diagram).drawio` or `video_production_company(physical_diagram).drawio`

---

## Lessions Learned

- How to create complex multi-location logical/physical networking diagrams.
- VLAN allocation and cable/device labelling. 
- How to create physical diagrams.
- When to use HCC vs VCC.
- IDF vs MDF.
- Supernetting and advanced subnetting concepts.
- Creating advanced IP adressing tables.
- Creating equipment lists.