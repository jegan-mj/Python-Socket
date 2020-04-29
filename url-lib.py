import urllib.request

try:
    headers = {}
    headers['User Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"

    req = urllib.request.Request("https://www.google.co.in", headers=headers)
    html = urllib.request.urlopen(req).read()

    print(html)

    print("Downloading file...")

    data = urllib.request.urlopen("https://wordpress.org/latest.zip").read()

    filename = "latest.zip"
    file_ = open(filename,"wb")
    file_.write(data)
    file_.close()
    print('Download completed')

except Exception as err:
    print("err",err)