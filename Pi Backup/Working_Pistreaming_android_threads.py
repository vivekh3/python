import io
import socket
import struct
import time
import picamera
import threading

listensocket=socket.socket()
Port=5004
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

                  
#client_socket.connect(('192.168.0.131', 8000))
connection = clientsocket.makefile('wb')

def cameratest():
    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (160, 120)
            camera.framerate = 30
            time.sleep(2)
            start = time.time()
            stream = io.BytesIO()
            # Use the video-port for captures...
            for foo in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                connection.write(struct.pack('<L', stream.tell()))
                #print(stream.tell())
                connection.flush()
                stream.seek(0)
                connection.write(stream.read())
                if time.time() - start > 30:
                    break
                stream.seek(0)
                #message=clientsocket.recv(1024).decode()
                #if message!='':
                #    print(message)
                stream.truncate()
                #message=clientsocket.recv(1024).decode()
                #if message!='':
                #    print(message)
        connection.write(struct.pack('<L', 0))

        

        #while True:
        #   time.sleep(1)
        #message=clientsocket.recv(1024).decode()
        
                
        #break
    finally:
        connection.close()
    #client_socket.close()
def accdata():
    while True:
        message=clientsocket.recv(1024).decode()
        if message!='':
            print(message)

t1=threading.Thread(target=cameratest)
t2=threading.Thread(target=accdata)

t1.start()
t2.start()
#t1.join()
#t2.join()
client_socket.close()
