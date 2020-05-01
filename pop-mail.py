import poplib
from email.message import EmailMessage

server = "127.0.0.1"
my_user = "kali"
passwd = "pythoncode"

server = poplib.POP3(server)
server.user(my_user)
server.pass_(passwd)

msgNum = len(server.list()[1])

for i in range(msgNum):
    for msg in server.retr(i+1)[1]:
        print(msg)
