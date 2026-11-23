# Backend firewall (pf)

Only the edge host may reach a backend port. Rules live in the pf anchor `teamx`, loaded from a copy of the system config so `/etc/pf.conf` itself is never edited.

| File | Purpose |
|---|---|
| `teamx.backend.laptop1.rules` | Backend A, port 3001 (copy of `/etc/pf.anchors/teamx.backend` on Laptop 1) |
| `teamx.backend.laptop2.rules` | Backend B, port 3002 (copy of `/etc/pf.anchors/teamx.backend` on Laptop 2) |
| `pf.conf.original` | Backup of the original `/etc/pf.conf`, kept for rollback |

`quick` makes the first matching rule final, so the pass rule for the edge is applied before the block rule. `block drop` discards packets without a reply, so a blocked client sees a timeout.

## Load

    sudo tee /etc/pf.anchors/teamx.backend > /dev/null < teamx.backend.laptopN.rules
    sudo sh -c 'cp /etc/pf.conf /etc/pf.conf.teamx; printf "anchor \"teamx\"\nload anchor \"teamx\" from \"/etc/pf.anchors/teamx.backend\"\n" >> /etc/pf.conf.teamx'
    sudo pfctl -nf /etc/pf.conf.teamx          # syntax check only
    sudo pfctl -e -f /etc/pf.conf.teamx
    sudo pfctl -a teamx -sr                    # show the active rules

## Roll back

    sudo pfctl -a teamx -F rules               # remove the teamx rules
    sudo pfctl -d                              # disable pf
    sudo pfctl -s info | head -1               # should say Status: Disabled
