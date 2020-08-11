import requests

base_url = "https://hacker-news.firebaseio.com"
sort_url = "orderBy=\"score\"&limitToFirst=50"

payload = "{}"

full_url = base_url + "/v0/newstories.json?" + sort_url

response = requests.request("GET", full_url, data=payload)

data = response.json()
print(response.text)