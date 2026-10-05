# TLS Certificate Setup Notes

We created our own local Certificate Authority (CA) with OpenSSL, used it to sign a
server certificate for app.teamX.test and api.teamX.test, and trusted the CA on both laptops.

## 1. Create the CA (Laptop 1)
openssl genrsa -out teamX-ca.key 2048
openssl req -new -key teamX-ca.key -out teamX-ca.csr -subj "/CN=TeamX Local CA"
openssl x509 -req -in teamX-ca.csr -signkey teamX-ca.key -out teamX-ca.crt -days 365 -sha256 -extfile ca.ext

## 2. Create the server certificate, signed by the CA
openssl genrsa -out app.teamX.test.key 2048
openssl req -new -key app.teamX.test.key -out app.teamX.test.csr -subj "/CN=app.teamX.test"
openssl x509 -req -in app.teamX.test.csr -CA teamX-ca.crt -CAkey teamX-ca.key -CAcreateserial -out app.teamX.test.crt -days 365 -sha256 -extfile san.ext

## 3. Verify
openssl verify -CAfile teamX-ca.crt app.teamX.test.crt
openssl x509 -in app.teamX.test.crt -noout -subject -issuer -dates -ext subjectAltName

## 4. Install in nginx
Certificate and key copied to /opt/homebrew/etc/nginx/certs/ and referenced by
ssl_certificate and ssl_certificate_key in teamx_phase1_https.conf.

## 5. Trust the CA (both laptops)
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain teamX-ca.crt

## Files in this folder
- teamX-ca.crt: CA certificate (public)
- app.teamX.test.crt: server certificate (public)
- ca.ext, san.ext: extension settings used when signing
Private keys (*.key) are NOT included and are never committed.
