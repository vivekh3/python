import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),5000))
s.listen(5)
while True:
    client,address=s.accept()
    print("Client IP"+client)
