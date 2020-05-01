import ftplib,os

def getfile(ftp,filename):

    try:
        ftp.retrbinary("RETR " + filename, open(filename,"wb").write)

    except Exception as err:
        print("Error downlaoding",err)

def uploadfile(ftp,filename):

    try:
        file_format = os.path.splitext(filename)[1]

        if file_format in (".html", ".csv", ".txt"):
            ftp.storlines("STOR " + filename, open(filename))
        else:
            ftp.storbinary("STOR " + filename, open(filename,"rb"), 1024)

    except Exception as all_errors:
        print("Err",all_errors)   
            
ftp = ftplib.FTP("ftp.nluug.nl")
ftp.login("anonymous", "password")

data = []

ftp.cwd("/pub/")
ftp.dir(data.append)

for directory in data:
    print("-" + directory)

print("Downloading")
getfile(ftp,"README.nluug")
print("Download completed")

print("Uploading")
uploadfile(ftp,"README.nluug")
print("Upload completed")

ftp.quit()
