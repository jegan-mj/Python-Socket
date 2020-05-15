import os,binascii,argparse,socket,socketserver

class tcpServer(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(512).strip()
        if data.startswith(b"send:"):
            fle = data.split(b":")[1]
            print("Receiving file.." + fle.decode())
            with open(str(fle.decode("utf-8")), "wb") as f:
                while data:
                    data = bytearray(self.request.recv(512)).strip()
                    if len(data) %2 == 0:
                        f.write(binascii.unhexlify(data))
                    else:
                        f.write(binascii.unhexlify(data.append(0)))
        print("File Received.")

def startServer(args):
    server = socketserver.TCPServer((args.ip,args.port), tcpServer)
    print("Sevrer Started")
    server.serve_forever()

def startClient(args):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((args.ip, args.port))
    path, fle = os.path.split(args.file)
    print("Sending file..",args.file)
    client.sendall(b"send:" + bytes(fle, "utf-8"))
    with open(args.file, "rb") as f:
        data = f.read(512)
        while(data):
            client.sendall(binascii.hexlify(data))
            data = f.read(512)
    f.close()
    print("File sent: ", args.file)

def main(args):
    if (args.client):
        startClient(args)
    elif(args.server):
        startServer(args)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--client", action="store", help = "start client", type=str, nargs='?', default=False, const=True)
    parser.add_argument("-s", "--server", action="store", help = "start server", type=str, nargs='?', default=False, const=True)
    parser.add_argument("-i", "--ip", action="store", help = "remote ip", type=str)
    parser.add_argument("-p", "--port", action="store", help = "remote port", type=int)
    parser.add_argument("-f", "--file", action="store", help = "files to send", type=str)

    args = parser.parse_args()

    if (not args.client and not args.server):
        parser.print_help()
        print("/n You must enter --server or --client")
        parser.exit()
    main(args)