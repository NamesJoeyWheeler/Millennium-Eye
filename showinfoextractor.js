from requests import get
print("----Millenium Eye----")
print("-Show Info Extractor-")
print("Developed By NamesJoeyWheeler")
print("")
var = input("Enter show link: ")
url = str(var)

response = get(url)
print("-----------------------------")
print(response.text[:500])
