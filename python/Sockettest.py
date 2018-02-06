import socket
Host='192.168.0.118'
Port=5000
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((Host,Port))
    s.sendall(b'Helloworld')
    data=s.recv(1024)
print('Recd',repr(data))
    
