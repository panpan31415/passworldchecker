import requests

url = "https://api.pwnedpasswords.com/range/" + "B48F2"

res = requests.get(url)

print(res)
