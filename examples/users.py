import requests

url = "https://hacker-news.firebaseio.com/v0/user/maxraz.json"

payload = "{}"
response = requests.request("GET", url, data=payload)

print(response.text)
