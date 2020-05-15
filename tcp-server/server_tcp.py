import socket

host = "127.0.0.1"
port = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen()

con,addr = s.accept()
print(type(con))
print(type(addr))

with con:
    print("Client connected ",addr)
    while True:
        data = con.recv(1024)
        if not data:
            break
        con.sendall(data)
