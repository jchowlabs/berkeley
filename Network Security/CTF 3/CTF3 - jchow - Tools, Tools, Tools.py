#####################
# Tools, Tools, Tools
#####################
import requests as req

response_list = []

for i in range(100):
    resp = req.get("http://w210.network:8005/flag.txt")
    response_list.append(resp.text)
    i = i + 1
        
print(response_list)

