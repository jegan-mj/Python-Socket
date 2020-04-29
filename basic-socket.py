import socket
try:
    print("Domain name: " + socket.getfqdn("8.8.8.8"))
    print("Host name to IP address: " + socket.gethostbyname("www.teezle.com"))
    print("Extended version of it: ",socket.gethostbyname_ex("www.teezle.com"))
    print("Name of the local machine: " + socket.gethostname())
except Exception as err:
    print("Error" + str(err))
