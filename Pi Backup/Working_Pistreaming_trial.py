import io
import socket
import struct
import time
import picamera
import cv2
import numpy as np


client_socket = socket.socket()
client_socket.connect(('192.168.0.131', 8000))
connection = client_socket.makefile('wb')
try:
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 30
        camera.vflip=True
        time.sleep(2)
        start = time.time()
        stream = io.BytesIO()
        print(type(stream))
        # Use the video-port for captures...
        for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            data = np.fromstring(stream.getvalue(), dtype=np.uint8)
            image=cv2.imdecode(data,1)
            height,width,channels=image.shape
            midheight=int(height/2)
            midwidth=int(width/2)
            im2=cv2.line(image,(0,midheight),(width,midheight),(0,255,0),2)
            im2=cv2.line(im2,(midwidth,0),(midwidth,height),(0,255,0),2)
            #image=image[:,:,::-1]
            #cv2.imshow('Test',image)
            image_stream=cv2.imencode('.jpeg',im2)[1].tostring()
            #print(type(image_stream))
            stream.write(image_stream)
            #print(type(stream))
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())
            if time.time() - start > 30:
                break
            stream.seek(0)
            stream.truncate()
    connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    client_socket.close()
    cv2.destroyAllWindows()
    print('Games Over')
