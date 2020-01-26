import io
import socket
import struct
import time
import picamera

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind(('',5000))
client,address=client_socket.accept()
print("Client IP: "+client)

                   
#client_socket.connect(('192.168.0.126', 8000))
connection = client_socket.makefile('wb')
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
