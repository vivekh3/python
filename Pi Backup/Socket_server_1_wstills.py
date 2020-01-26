#import io
#import socket

import socket
import time
import base64
from socket import gethostbyname, gethostname
from picamera import PiCamera
import os
camera=PiCamera()
times=0
camera.resolution=(160,120)

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
times=0

while (times<1):
    camera.capture('/home/pi/Desktop/image'+str(times)+'.jpg')
    imagesize=os.path.getsize('/home/pi/Desktop/image'+str(times)+'.jpg')
    print(os.path.getsize('/home/pi/Desktop/image'+str(times)+'.jpg'))
    clientsocket.send(bytes(str(imagesize),"utf-8"))    
    #time.sleep(3)
    datatobesent=open(('/home/pi/Desktop/image'+str(times)+'.jpg'),"rb").read()
    clientsocket.send(datatobesent)

    
    
    msg="The time is "+str(time.time())+"\n"
    print(msg)
    
    #clientsocket.send(bytes(msg,"utf-8"))
    times+=1
    
        
listensocket.close()

clientsocket.close()



    