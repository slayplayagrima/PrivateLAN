# TLS notes (Phase 2)

The certificate authority and server certificate from Phase 1 are reused. Nothing was re-issued.

- The certificate is issued for the names `app.teamX.test` and `api.teamX.test`, not for an IP address. Changing the laptop IPs or moving the edge to another laptop therefore does not affect it.
- The standby edge on Laptop 2 serves the same names, so it uses the same certificate and private key, placed in `/opt/homebrew/etc/nginx/certs/` and referenced by `ssl_certificate` and `ssl_certificate_key` in its nginx config.
- Both laptops already trust the TeamX Local CA, so a client sees no certificate warning from either edge.
- Private keys (`*.key`) are copied between the laptops directly and are never committed to the repository.

Creation steps for the CA and the certificate: `CN_Phase1/2_Config_Bundle/tls/README.md`.
