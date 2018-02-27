import urllib.request

print("----Millenium Eye----")
print("----Sub Downloader----")
print("Developed By NamesJoeyWheeler")
print(" ")
var = input("Enter Subtitle Link: ")
def downloadfile():
  urllib.request.urlretrieve(str(var), "eng.vtt")

downloadfile()
