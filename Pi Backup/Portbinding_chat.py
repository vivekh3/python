import socket
import sys
from _thread import *
Host = ''
Port = 5000

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    s.bind((Host,Port))

except socket.error as msg:
    print ("Binding Failed")

print ("Binding complete")

s.listen(5)

print ("Waiting for a connection")

def threaded_client(conn):
    conn.send (str.encode('Welcome.! Please enter your info'))

    while True:
        data=conn.recv(2048)
        reply="Server response :"+data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()


while True:
    conn,addr = s.accept()
    print ('Connected with'+addr[0]+':'+str(addr[1]))
    start_new_thread(threaded_client,(conn,))
