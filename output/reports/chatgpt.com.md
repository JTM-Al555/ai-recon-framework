# AI Recon Report

Target:
chatgpt.com

Generated:
2026-05-12 11:39:27.062699


## dns

```json
{'A': ['172.64.155.209', '104.18.32.47'], 'AAAA': ['2a06:98c1:3100::6812:202f', '2a06:98c1:310b::ac40:9bd1'], 'MX': ['No record found'], 'NS': ['hassan.ns.cloudflare.com.', 'savanna.ns.cloudflare.com.'], 'TXT': ['"google-site-verification=3p_zWfTXlQ4Mbxvq51ylW59LjgneYCB_vXpS-DLIEwM"', '"google-site-verification=qz8yKZH1f2h4Dl7S-nRAo0immoInmiosRhyjUxXuUOs"', '"google-site-verification=rZodbEw8Hlw3gg7Z7mxkmQUNPnO_1khlohRX5D6qeUo"', '"google-site-verification=u3JFUrrlvyiaVlGsdIRMgmuvDluR6gC-TIPBEQLbl8c"', '"google-site-verification=vHr-4wFDXLd3wze6i0YimpiGHC1u0Hy3x1dGAiyeHWs"', '"v=spf1 -all"'], 'CNAME': ['No record found']}
```


## http

```json
{'url': 'https://chatgpt.com', 'status_code': 403, 'headers': {'server': 'cloudflare', 'content-type': 'text/html; charset=UTF-8', 'content-length': 'Not Present', 'x-powered-by': 'Not Present'}, 'response_size': 8505}
```


## web_crawler

```json
[{'url': 'https://chatgpt.com/', 'status': 403, 'content_length': 8420}, {'url': 'https://chatgpt.com/login', 'status': 403, 'content_length': 8435}, {'url': 'https://chatgpt.com/admin', 'status': 403, 'content_length': 8435}, {'url': 'https://chatgpt.com/dashboard', 'status': 403, 'content_length': 8447}, {'url': 'https://chatgpt.com/api', 'status': 403, 'content_length': 8429}, {'url': 'https://chatgpt.com/robots.txt', 'status': 200, 'content_length': 3422}, {'url': 'https://chatgpt.com/sitemap.xml', 'status': 403, 'content_length': 8474}, {'url': 'https://chatgpt.com/graphql', 'status': 403, 'content_length': 8441}, {'url': 'https://chatgpt.com/auth', 'status': 403, 'content_length': 8432}, {'url': 'https://chatgpt.com/register', 'status': 403, 'content_length': 8444}]
```


## javascript_analysis

```json
[]
```


## ports

```json
[{'port': 25, 'service': 'SMTP', 'status': 'open'}, {'port': 80, 'service': 'HTTP', 'status': 'open'}, {'port': 443, 'service': 'HTTPS', 'status': 'open'}, {'port': 8080, 'service': 'HTTP-ALT', 'status': 'open'}]
```


## subdomains

```json
[{'subdomain': 'https://www.chatgpt.com', 'status': 301}, {'subdomain': 'https://api.chatgpt.com', 'status': 404}]
```


## ssl

```json
{'issuer': ((('countryName', 'US'),), (('organizationName', 'Google Trust Services'),), (('commonName', 'WE1'),)), 'subject': ((('commonName', 'chatgpt.com'),),), 'expires': 'Aug  7 00:51:52 2026 GMT', 'valid': True}
```


## security_headers

```json
{'Content-Security-Policy': {'present': False, 'value': 'Missing'}, 'Strict-Transport-Security': {'present': False, 'value': 'Missing'}, 'X-Frame-Options': {'present': False, 'value': 'Missing'}, 'X-Content-Type-Options': {'present': False, 'value': 'Missing'}, 'Referrer-Policy': {'present': False, 'value': 'Missing'}}
```


## technologies

```json
['Cloudflare']
```


## cves

```json
{}
```


## ai_analysis

```json
{'timestamp': '2026-05-12 11:39:27.059896', 'risk_score': 2, 'summary': 'Low to moderate risk detected.', 'findings': ['DNS data collected', 'Some open ports detected', 'HTTP endpoint reachable', 'SSL certificate info collected'], 'recommendations': []}
```

