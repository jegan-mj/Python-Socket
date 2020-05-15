import sys, socket, random

class IRC():

    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def send(self, chan, msg):
         
        self.irc.send(("PRIVMSG " + chan + " :" + msg + "\n").encode())

    def connect(self,server,chan,botnick):

        print("Connecting to the server: " + server)
        self.irc.connect((server,6667))
        
        self.irc.send(("USER " + botnick + " " + botnick + " " + botnick + " :New bot! \n").encode())
        self.irc.send(("NICK " + botnick + "\n").encode())
        self.irc.send(("JOIN " + chan + "\n").encode())

    def get_text(self):

        text = self.irc.recv(2040)
        return text

channel = "#jchannel12345"
server = "irc.freenode.com"
nickname = "chitti"

irc = IRC()
irc.connect(server,channel,nickname)

while True:
    message = irc.get_text()
    print(message.decode())
    if b"PRIVMSG" in message and channel.encode() in message and b":hello" in message:
        user = message.strip().split(b"~")[0][1:-1].decode()
        irc.send(channel, "Hello " + user + ". Welcome!! \n")