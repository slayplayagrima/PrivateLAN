# 2_Config_Bundle

Final configuration files as they run on each laptop. No private keys.

| Subfolder | File | Owner | Source on the laptop |
|---|---|---|---|
| `dnsmasq_primary/` | `dnsmasq_primary.conf` | Agrima | `/opt/homebrew/etc/dnsmasq.conf` |
| `dnsmasq_backup/` | `dnsmasq_backup.conf` | Gargi | `/opt/homebrew/etc/dnsmasq.conf` |
| `nginx_primary/` | `teamx_primary.conf` | Agrima | `/opt/homebrew/etc/nginx/servers/teamx.conf` |
| `nginx_standby/` | `teamx_standby.conf` | Gargi | `/opt/homebrew/etc/nginx/servers/teamx.conf` |
| `firewall/` | `pf.conf.original`, `teamx.backend.laptop1.rules` | Agrima | `/etc/pf.conf`, `/etc/pf.anchors/teamx.backend` |
