import socket
try:
    print("Domain name: " + socket.getfqdn("8.8.8.8"))
    print("Host name to IP address: " + socket.gethostbyname("dns.google"))
    print("Extended version of it: ",socket.gethostbyname_ex("dns.google"))
    print("Name of the local machine: " + socket.gethostname())
except Exception as err:
    print("Error" + str(err))
