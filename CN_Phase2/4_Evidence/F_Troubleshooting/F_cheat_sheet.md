# Troubleshooting cheat sheet

Check from the bottom of the request upwards. Stop at the first layer that fails, say what you see, then fix or isolate it.

| Step | Question | Command | What a failure looks like |
|---|---|---|---|
| 1 DNS | Does the name resolve, and from which server? | `dig app.teamX.test` | NXDOMAIN, timeout, or the wrong IP |
| 2 IP | Can we reach that address? | `ping 10.7.1.45` | No replies |
| 3 TCP | Is something listening on the port? | `nc -vz 10.7.1.45 443` | Refused (nothing listening) or timeout (firewall drop) |
| 4 TLS | Is the certificate valid for the name? | `curl -v https://app.teamX.test` | Certificate or handshake error |
| 5 App | Do nginx and the backends answer? | `curl -sS -i https://app.teamX.test/api/status` | 502, 404, wrong `X-Backend` or `X-Edge` |

## Quick reads

- Resolves to the wrong IP: the DNS record or a stale cache. Check `dig @10.7.1.45` and `dig @10.7.17.119`, then flush the client cache.
- Ping works but port 443 is refused: nginx is down or listening on another port. `sudo lsof -iTCP:443 -sTCP:LISTEN -n -P`
- Port times out (no refusal): a firewall is dropping it. `sudo pfctl -a teamx -sr`
- Certificate error: the name does not match, or the CA is not trusted on that laptop.
- 502 from nginx: DNS, TCP and TLS are fine, the backends are not. `grep "connect() failed" /opt/homebrew/var/log/nginx/error.log | tail`
- `X-Edge` says which edge answered (primary or standby) and `X-Backend` says which backend (A or B).
- A curl that prints nothing: use `-sS`, since `-s` alone hides the error.

## Say out loud

1. Which layer I am checking and why.
2. What I expect to see.
3. What I actually see, and what that rules out.
