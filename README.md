# Transip-API-v6
---
This repo contains a package for Python3 to connect to the API of transip.

For more information about the Transip API go to https://api.transip.nl/rest/docs.html

Currently this is package mainly supports all actions on DNS. It can be easily extended.

Example python code:
<pre><code>#!/usr/bin/env python3
import requests
import json
import transip_api_v6

login          = 'username'       # Username from Transip
keyfile        = 'test copy.pem'  # Key generated @ Transip API page
domain         = 'gemert.net'     # Domain it concers
find_dns_entry = 'home-server'    # Domain entry on which you want to access

# Get public IP
res = requests.get('https://ipinfo.io')
if res.status_code != 200:
    print('Failed to get public ip.')
    exit(1)
pub_ip=json.loads(res.text)['ip']

# Get Header for authentication against transip api V6
key_file = open(keyfile, "r")
key = key_file.read()
key_file.close()
# ph = transip_api_v6.Generic(login, key)
headers = transip_api_v6.Generic(login, key).get_headers()

# Request DNS entries for this domain
dns_entries = domains.list_dns_entries(domain)

# Find entry
found_dns_entries = []
for dns_entry in dns_entries['dnsEntries']:
  if dns_entry['name'] == find_dns_entry and dns_entry['type'] == 'A':
    found_dns_entries.append(dns_entry)

# Change entry for this domain with current public IP
if len(found_dns_entries) == 0:
  data = '''{
    "dnsEntry": {
      "name": "''' + find_dns_entry + '''",
      "expire": 300,
      "type": "A",
      "content": "''' + pub_ip + '''"
    }
  }
  '''
  domains.add_dns_entry(domain, data)
elif len(found_dns_entries) == 1:
  if found_dns_entries[0]['content'] == pub_ip:
    print('No change needed')
  else:
    print('Change dns entry')
    print('From: ' + json.dumps(found_dns_entries[0]))
    found_dns_entries[0]['content'] = pub_ip
    print('To  : ' + json.dumps(found_dns_entries[0]))
    domains.update_dns_entry(domain, '{"dnsEntry": ' + json.dumps(found_dns_entries[0]) +'}')
else:
  print('Multiple entries found, can\'t determine which to change (if any).')

</code></pre>
