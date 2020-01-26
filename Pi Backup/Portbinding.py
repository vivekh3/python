import socket
import sys

Host = ''
Port = 5000

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    s.bind((Host,Port))

except socket.error as msg:
    print ("Binding Failed")

print ("Binding complete")

s.listen(5)

conn,addr = s.accept()

print ('Connected with'+addr[0]+':'+str(addr[1]))
