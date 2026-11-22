# Private Network Service Platform – Team X

Agrima (Laptop 1: DNS + nginx edge + Backend A) · Gargi (Laptop 2: Backend B + client)

## Phase 1
- Architecture Document: CN_Phase1/1_Architecture_Document/
- Configuration Bundle: CN_Phase1/2_Config_Bundle/ (dnsmasq, nginx, TLS notes, startup instructions)
- Backend Source Code: CN_Phase1/3_Backend_Code/ (backend-a: Python, backend-b: Flask)
- Evidence: CN_Phase1/4_Evidence/
  - A_LAN · B_DNS · C_D_Backends_LoadBalancing · E_TLS · F_Caching · G_Wireshark · H_Failure_Scenarios
- Demo video: <add Google Drive link>

## Phase 2
Extensions: A backup DNS · B TTL and caching · C backend isolation (firewall) · D backend failover · E standby edge and cutover · F troubleshooting drill
- Architecture Update: CN_Phase2/1_Architecture_Update/
- Configuration Bundle: CN_Phase2/2_Config_Bundle/ (dnsmasq primary and backup, nginx primary and standby, firewall rules)
- Final Report: CN_Phase2/3_Final_Report/
- Evidence: CN_Phase2/4_Evidence/
  - A_Backup_DNS · B_TTL · C_Isolation · D_HA_Failover · E_Edge_Migration · F_Troubleshooting
- Folder guide: CN_Phase2/README.md
