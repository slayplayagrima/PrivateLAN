# 2_Config_Bundle

Final configuration files as they run on each laptop. No private keys.

## Config files

| Subfolder | File | Owner | Source on the laptop |
|---|---|---|---|
| `dnsmasq_primary/` | `dnsmasq_primary.conf` | Agrima | `/opt/homebrew/etc/dnsmasq.conf` |
| `dnsmasq_backup/` | `dnsmasq_backup.conf` | Gargi | `/opt/homebrew/etc/dnsmasq.conf` |
| `nginx_primary/` | `teamx_primary.conf` | Agrima | `/opt/homebrew/etc/nginx/servers/teamx.conf` |
| `nginx_standby/` | `teamx_standby.conf` | Gargi | `/opt/homebrew/etc/nginx/servers/teamx.conf` |
| `firewall/` | `teamx.backend.laptop1.rules`, `teamx.backend.laptop2.rules`, `pf.conf.original` | Both | `/etc/pf.anchors/teamx.backend`, `/etc/pf.conf` |

## Notes

| File | What it covers |
|---|---|
| `launch_instructions_phase2.md` | Start order and checks for both laptops, with the Phase 2 IPs |
| `tls_notes_phase2.md` | What changed for TLS in Phase 2 (standby uses the same certificate) |
| `firewall/README.md` | Rule explanation, how to load them, and how to roll back |

TLS certificate creation steps and the Phase 1 backend code are unchanged. See `CN_Phase1/2_Config_Bundle/tls/README.md` and `CN_Phase1/3_Backend_Code/`.

## Phase 2 addresses

| | Laptop 1 | Laptop 2 |
|---|---|---|
| IP | 10.7.1.45 | 10.7.17.119 |
| Roles | Primary DNS, primary edge, Backend A | Backup DNS, standby edge, Backend B, client |
