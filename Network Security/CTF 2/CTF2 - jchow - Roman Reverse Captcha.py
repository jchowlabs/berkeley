########################
# Roman Reverse Captcha
########################

import re
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("w210.network", 8002))

s.send(b"16\n")
s.send(b"65536\n")
s.send(b"4194304\n")

while True:
    
    data = s.recv(1024).decode()
    identity_index = data.find("identity")
    hiccup_index = data.find("hiccups")
    print(data)
    
    if identity_index > 193: 
        
        # Searches for + operator in equation.
        digit = re.findall(r'\d+', data) 
        
        # Initializes variables with elements of equation.
        element1 = digit[0]
        element2 = digit[1]
        element3 = digit[2]
        element4 = digit[3]
        element5 = digit[4]
        element6 = digit[5]
        
        # Transform element to integers, then adds them together.
        equation1 = int(element1) + int(element2)
        equation2 = int(element3) + int(element4)
        equation3 = int(element5) + int(element6)
        
        # Appends \n character to each equation.
        message4 = str(equation1) + '\n'
        message5 = str(equation2) + '\n'
        message6 = str(equation3) + '\n'
        
        # Sends formatted answers back to CTF system.
        s.send(message4.encode())
        s.send(message5.encode())
        s.send(message6.encode())
    
    # Executes code to handle third set of equations.
    # The word 'hiccups' only appears in third challenge.
    if hiccup_index > 38:
        
        # This code segment handles the first equation.
        # The code gets chunks of data from CTF system, 
        # formats the data so the digits can be added, 
        # then sends the answer back to CTF system. 
        fragments = []
        done = False
        
        while (not done):
            chunk = s.recv(1024).decode()
            if ('\n' in chunk): # Removes \n character
                done = True
                break
            else:
                fragments.append(chunk) # Appends chunk to list       
            
        message = "".join(fragments) # Re-assembles digits 
        words = message.split()
        element1 = words[1]
        element2 = words[3]
        equation4 = int(element1) + int(element2) # Adds numbers
        message1 = str(equation4) + '\n' # Adds \n character
        s.send(message1.encode()) # Sends answer to CTF system
        
        # This code segment handles the second equation. 
        # The code performs the same logic as described
        # for equation one above. 
        fragments = []
        done = False
        chunk = ""
        message = ""
        words = ""
        element1 = ""
        element2 = ""
        message1 = ""
        
        while (not done):
            chunk = s.recv(1024).decode()
            print('')
            if ('\n' in chunk):
                done = True
                break
            else:
                fragments.append(chunk)          

        message = chunk
        words = message.split()
        element1 = words[1]
        element2 = words[3]
        equation4 = int(element1) + int(element2)
        message1 = str(equation4) + '\n'
        s.send(message1.encode())
        
        # This code segment handles the third equation. 
        # The code performs the same logic as described
        # for equation one above. 
        fragments = []
        done = False
        chunk = ""
        message = ""
        words = ""
        element1 = ""
        element2 = ""
        message1 = ""
        
        while (not done):
            chunk = s.recv(1024).decode()
            print('')
            if ('\n' in chunk):
                done = True
                break
            else:
                fragments.append(chunk)  
                
        message = chunk
        words = message.split()
        element1 = words[1]
        element2 = words[3]
        equation4 = int(element1) + int(element2)
        message1 = str(equation4) + '\n'
        s.send(message1.encode())
        
        # This code segment handles the fourth equation. 
        # The code performs the same logic as described
        # for equation one above. 
        fragments = []
        done = False
        chunk = ""
        message = ""
        words = ""
        element1 = ""
        element2 = ""
        message1 = ""
        
        while (not done):
            chunk = s.recv(1024).decode()
            if ('\n' in chunk):
                done = True
                break
            else:
                fragments.append(chunk)          
            
        message = chunk
        words = message.split()
        element1 = words[1]
        element2 = words[3]
        equation4 = int(element1) + int(element2)
        message1 = str(equation4) + '\n'
        s.send(message1.encode())

s.close() # Closes socket connection.
