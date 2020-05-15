import paramiko

hostname = "127.0.0.1"
port = 22
username = "kali"
passwd = "8520"

src = "/home/kali/Python/latest.zip"
sav = "/home/kali/Python/python-socket/download.zip"
upl = "/home/kali/Python/python-socket/upload.zip"

try:
    client = paramiko.Transport(hostname,port)
    client.connect(username=username,password = passwd)
    print("Connected through ssh")

    sftp = paramiko.SFTPClient.from_transport(client)
    print("Starting download")
    sftp.get(src,sav)
    print("Downloaded")

    print("Uploading file")
    sftp.put(src,upl)
    print("Uploaded")

    client.close()
    print("Disconnected")


except Exception as err:
    print("Error",err)