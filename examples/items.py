import requests

url = "https://hacker-news.firebaseio.com/v0/item/24050651.json"

payload = "{}"
response = requests.request("GET", url, data=payload)

print(response.text)