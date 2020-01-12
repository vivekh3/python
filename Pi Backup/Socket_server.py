import socket
import time
from socket import gethostbyname, gethostname

listensocket=socket.socket()
Port=5000
maxConnections=999
IP=socket.gethostname()
print(IP)
listensocket.bind(('',Port))
listensocket.listen(maxConnections)
print('Server started at '+IP+' on Port'+str(Port))
(clientsocket,address)=listensocket.accept()
print("New Connection Made: "+str(address))
listensocket.close()
running=True
while running:
    message=clientsocket.recv(1024).decode()
    while True:
        time.sleep(1)
        #message=clientsocket.recv(1024).decode()
        if message!='':
            print(message)
            break

    print(message)
#listensocket.close()
            
        
    
    
            


