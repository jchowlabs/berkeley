#####################
# For Your Eyes Only
#####################

from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("w210.network",8001))

while True:
    data = s.recv(1024).decode()
    print(data)
    if not data:
        quit()
    else:
        s.send(b"But not at St. Moritz") # Secret message encoded in byte stream
        break # Break out of loop

s.close() # Closes socket


