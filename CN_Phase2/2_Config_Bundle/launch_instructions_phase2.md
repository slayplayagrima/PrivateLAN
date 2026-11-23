# Launch instructions (Phase 2)

Addresses: Laptop 1 = 10.7.1.45, Laptop 2 = 10.7.17.119. The college Wi-Fi hands out addresses automatically, so check both before every session:

    ipconfig getifaddr en0

If an address changed, update the DNS records (`host-record=` lines), the `server` lines in the nginx upstream block, and the firewall rule files, then restart the services.

## Laptop 1 (Agrima): primary DNS, primary edge, Backend A

    sudo brew services restart dnsmasq
    sudo nginx -t && sudo brew services restart nginx
    cd CN_Phase1/3_Backend_Code/backend-a && python3 backend.py A 3001

## Laptop 2 (Gargi): backup DNS, standby edge, Backend B, client

    sudo brew services restart dnsmasq
    sudo nginx -t && sudo brew services restart nginx
    cd CN_Phase1/3_Backend_Code/backend-b
    source venv/bin/activate && python app.py

Client DNS list (primary first, backup second), then flush the cache:

    sudo networksetup -setdnsservers Wi-Fi 10.7.1.45 10.7.17.119
    sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
    networksetup -getdnsservers Wi-Fi

## Checks (from Laptop 2)

    dig app.teamX.test +short
    for i in 1 2 3 4; do curl -sS -i https://app.teamX.test/api/status | grep -iE "^HTTP|x-backend|x-edge"; done

Expected: `x-backend` alternates A and B, and `x-edge` is `primary`.

## Before disconnecting from the network

    sudo networksetup -setdnsservers Wi-Fi empty
