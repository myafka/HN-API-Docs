import requests

def extract_score(json):
    try:
        return int(json['score'])
    except KeyError:
        return 0

base_url = "https://hacker-news.firebaseio.com"

payload = "{}"

newstories_url = base_url + "/v0/newstories.json"

newstories_response = requests.request("GET", newstories_url, data=payload)

data = newstories_response.json()
cut_data = data[:50]

items_list = []

for item_id in cut_data:
    item_url = base_url + "/v0/item/%d.json" % item_id
    item_response = requests.request("GET", item_url, data=payload)
    items_list.append(item_response.json())


items_list.sort(key=extract_score, reverse=True)

print(items_list)
