import socket

host = "127.0.0.1"
port = 8081

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.sendall("Hello python world")

data = s.recv(1024)

print("Received data",data)
    


