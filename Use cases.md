<h1>Use cases</h1>

This section contains examples of API usage. The examples in this guide are written in Python 3. You can use any programming language to work with the API.

If you are a new to this API, we recommend starting with [Getting started](https://github.com/myafka/HackerNewsDocs/blob/master/Getting%20started.md).

<h2>Fetch 50 stories</h2>

Imagine that you need to select 50 new stories. Since the [New Stories method](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#new-stories) returns 500 stories, you will need to take addional steps.

Example request:

```
import requests

base_url = "https://hacker-news.firebaseio.com"

payload = "{}"

full_url = base_url + "/v0/newstories.json"

response = requests.request("GET", full_url, data=payload)

data = response.json()
cut_data = data[:50]

print(cut_data)
```
In response, you will get an array of 50 IDs of the stories.

```
[
    24065859, 24065853, 24065843, 24065838, 24065834, ... ,24065260
]
```

  
<h2>Sorted stories</h2>

In this example, we order stories in a descending order, sorted by score.

Example request:
 
```
import requests

def  (json):
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
```

In response, you will get a sorted array.

```
[{'by': 'ElectronShak', 'descendants': 9, 'id': 24065379, 'kids': [24065844, 24065880, 24065860, 24065865, 24065752, 24065777, 24065637], 'score': 46, 'time': 1596660235, 'title': 'Why there’s so little left of the early internet', 'type': 'story', 'url': 'https://www.bbc.com/future/article/20190401-why-theres-so-little-left-of-the-early-internet'}, 
{'by': 'networkimprov', 'descendants': 2, 'id': 24065499, 'kids': [24065876, 24065868], 'score': 18, 'time': 1596660961, 'title': 'Go File System Interfaces, draft design', 'type': 'story', 'url': 'https://go.googlesource.com/proposal/+/master/design/draft-iofs.md'}, 
..., 
{'by': 'sumitg12', 'descendants': 0, 'id': 24065308, 'score': 1, 'time': 1596659900, 'title': 'Auto Labeling for Images', 'type': 'story', 'url': 'https://developer.ibm.com/technologies/artificial-intelligence/blogs/ibm-cloud-annotations-tool-eases-the-process-of-ai-data-labeling/'}]
```

Well done! The story "Why there’s so little left of the early internet" has the bigest score.

<h2>Create a mobile app</h2>

Our API uses Firebase. Firebase serves as a database that changes in real-time and stores data in JSON. Any changes to the database are immediately synced between all clients or devices that use the same database. 

You can use Firebase SDK to create a mobile app for Android and iOS. To get started, visit the [Firebase setup instructions](https://firebase.google.com/docs/).

Here is an example of a [Swift app](https://github.com/timshim/Hackery).
