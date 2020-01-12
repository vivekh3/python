import socket
import time
import base64
from socket import gethostbyname, gethostname

listensocket=socket.socket()
Port=5001
maxConnections=999
IP=socket.gethostname()
print(IP)
listensocket.bind(('',Port))
listensocket.listen(maxConnections)
print('Server started at '+IP+' on Port'+str(Port))
(clientsocket,address)=listensocket.accept()
print("New Connection Made: "+str(address))
#listensocket.close()
running=True
times=1
while running:
    time.sleep(3)
    msg="The time is "+str(time.time())+"\n"
    print(msg)
    
    clientsocket.send(bytes(msg,"utf-8"))
    times+=1
    if (times==10):
        running=False
        #listensocket.close()
        
listensocket.close()
            
        
    
    
            


