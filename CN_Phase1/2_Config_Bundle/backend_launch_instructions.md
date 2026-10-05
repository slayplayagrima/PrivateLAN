# Startup Instructions

## Laptop 1 (10.7.27.219): DNS + Edge + Backend A
sudo brew services restart dnsmasq
sudo brew services restart nginx
cd CN_Phase1/3_Backend_Code/backend-a && python3 backend.py A 3001

## Laptop 2 (10.7.5.228): Backend B + Client
sudo networksetup -setdnsservers Wi-Fi 10.7.27.219
cd CN_Phase1/3_Backend_Code/backend-b
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
python app.py

## Check (from Laptop 2)
for i in 1 2 3 4; do curl -s -i https://app.teamX.test/api/status | grep x-backend; done
