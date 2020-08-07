<h1>Overview</h1>

The HackerNews API is used for getting information from the site [HackerNews](https://news.ycombinator.com). The API was built using Firebase. 


* [Get started](https://github.com/myafka/Test/blob/master/Getting%20started.md)

* Get to know [about site] Hacker News

* Learn about API [methods](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md)

* Read about other [use cases](https://github.com/myafka/HackerNewsDocs/blob/master/Use%20cases.md)


<h1>Getting started</h1>

You can use this API to get information from the site https://news.ycombinator.com. For example, a list of the most popular stories or the title and URL of a story.

Examples in this guide are written in Python 3. You can use any programming language to work with the API.

<h2>Step 1. The top stories</h2>

Let's find out what stories are in the top right now. To do this, we need the [Top Stories method](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#top-stories). You don't need to set path parameters in this method.
 
Example request:

```
import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

payload = "{}"
response = requests.request("GET", url, data=payload)

print(response.text)
```
In response, you will get an array with the IDs of the top stories.

Example response:

```
[
    24050651, 24049428, 24049593, 24050691, 24049349, ..., 24009672
]
```
In addition to the top stories you can get the newest stories, the best stories, the top ask stories, the show stories and the latest jobs posted. All these methods return an array with the IDs.

<h2>Step 2. The information about the item</h2>

The ID is a very important and useful entity that binds everything together. Using the ID, you can find the desired story. For example, let's see what is so special about the ID 24050651 story because it is so popular.

To do this, we need the [Items method](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#items). In this method, you need to set ID as a path parameter.

Example request:

```
import requests

url = "https://hacker-news.firebaseio.com/v0/item/24050651.json"

payload = "{}"
response = requests.request("GET", url, data=payload)

print(response.text)
```

Example response:

```
{
  "by" : "maxraz",
  "descendants" : 44,
  "id" : 24050651,
  "kids" : [ 24051165, 24051909, 24050809, 24050939, 24050843, 24051198, 24050902, 24050852, 24051144, 24050827, 24050965, 24052048, 24050799, 24051528, 24051126, 24051023, 24051363, 24050948, 24051836, 24051151, 24051277, 24050989, 24050825, 24051423, 24052145, 24050847 ],
  "score" : 144,
  "time" : 1596553275,
  "title" : "Show HN: Visualize Graph Theory",
  "type" : "story",
  "url" : "https://treksit.netlify.app/"
}
```

Hm, "Show HN: Visualize Graph Theory", sounds interesting!

The HakerNews site has not only storis, but also: jobs, comments, polls or pollopts. You can also get data about them using this method, you just need to change the ID.

<h2>Step 3. The information about the user</h2>

To get data about a user, you need the [Users method](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#users). In this method, you need to set user ID.
For example, we can find information about the author of the most popular story. His user ID is maxraz.

Example request:

```
import requests

url = "https://hacker-news.firebaseio.com/v0/user/maxraz.json"

payload = "{}"
response = requests.request("GET", url, data=payload)

print(response.text)

```

Example response:

```
{
  "about" : "Web designer and dev",
  "created" : 1501496241,
  "id" : "maxraz",
  "karma" : 550,
  "submitted" : [ 24059825, 24050790, 24050651, 24048586, 24039297,..., 14890739 ]
}

```
Now we know that maxraz has a good karma and he has many other stories. If you are interested, you can see what they are about using the method from Step 2.

<b>What's next</b>

* [Learn about API methods](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md)

* [Read about other use cases](https://github.com/myafka/HackerNewsDocs/blob/master/Use%20cases.md)


<h1>About Hacker News</h1>

Hacker News is a social news site focusing on computer science and entrepreneurship. 

The site has several items of content:

* story - post with a link to an interesting article, there are several subtypes:
  * ask - post with text for discussion
  * show - post with something that you've made
* job - thread where you can post job offers
* comment - self-explanatory
* poll - a survey with set of answer options, each answer is a pollopt

The site has several collections of stories: 
* top stories (https://news.ycombinator.com/news) - top of the recent stories  
* newest stories (https://news.ycombinator.com/newest) - recently published stories 
* best stories (https://news.ycombinator.com/top)- best of the best stories 

<h1>Methods</h1>

This section contains description of HackerNews API. If you don't know anything about site HackerNews, at first read the article [About](https://github.com/myafka/Test/blob/master/About.md).


| Method      | Description |
| ------------- |-------------|
| [items](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#Items) | Returns the information about the item (job, story, comment, poll or pollopt). |
| [users](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#Users) | Returns the current user's HakerNews profile. |
| [maxitem](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#max-item-id) | Returns the current largest item ID. |
| [topstories](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#top-stories) | Returns the top of recent stories posted on HakerNews. |
| [newstories](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#new-stories) | Returns the newest stories posted on HakerNews. |
| [beststories](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#bests-stories) | Returns the best stories posted on HakerNews. |
| [askstories](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#asks-stories) | Returns the ask stories posted on HakerNews. |
| [showstories](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#shows-stories) | Returns the show stories posted on HakerNews. |
| [jobstories](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#job-stories) | Returns the latest jobs posted on HakerNews. |
| [updates](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#updates) | Returns item IDs and users IDs where there were changes. |


<h2>Items</h2>

Returns the information about the item (job, story, comment, poll or pollopt).

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty`

<h3>Path parameters</h3>

|Parameter | Type | Description |
| ------------- |-------------|--------|
| id | integer | Required. The item's unique identifier. |

<h3>Query parameters</h3>

|Parameter | Type | Description |
| ------------- |-------------|--------|
| print | string | Optional. 'pretty'- returns the data in a human-readable format. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data). |

<h3>Response</h3>

`HTTP Code: 200 - OK`

```
{
  "by": "string",
  "dead": boolean,
  "descendants": integer,
  "id": integer,
  "score": integer,
  "time": integer,
  "title": "string",
  "type": "string",
  "url": "string"
}
```

|Parameter    | Type | Description | Story | Job | Comment | Poll |Pollopt|
| ------------- |-------------|--------|--------|--------|--------|--------|--------|
| id   | integer | Required. The item's unique ID.|✔|✔|✔|✔|✔|
| deleted | boolean | Optional. 'true' - if the item is deleted.  |✔|✔|✔|✔|✔|
| type | string | Required. The type of item. Possible values: "job", "story", "comment", "poll", or "pollopt".    |✔|✔|✔|✔|✔|
| by | string | Optional. The user ID of the item's author.    |✔|✔|✔|✔|✔|
| time | integer | Optional. Creation date of the item, in [Unix Time](http://en.wikipedia.org/wiki/Unix_time).    |✔|✔|✔|✔|✔|
| text | string | Optional. The comment, story or poll text.    |✔|✔|✔|✔|✔|
| dead | boolean | Optional. 'true' - if the item is dead. |✔|✔|✔|✔|✔|
| parent | integer | Optional. The items parent. |||✔||✔|
| poll | integer | Optional. The pollopt's associated poll. |||||✔|
| kids | array[integer] | Optional. The IDs of the item's comments, in ranked display order. |✔|✔|✔|✔|✔|
| url | string | Optional. The URL. |✔|✔||||
| score | integer | Optional. The score for a story, or the votes for a pollopt. |✔|||✔|✔|
| title | string | Optional. The title of the story, poll or job.    |✔|✔||✔||
| parts | array[integer] | Optional. A list of related pollopts, in the display order.    ||||✔||
| descendants | integer | Optional. The total comment count.    |✔|||✔||

<h3>Example</h3>

<h4>Request</h4>

  `GET https://hacker-news.firebaseio.com/v0/item/88.json?print=pretty`
  
<h4>Response</h4>

`HTTP Code: 200 - OK`

``` 
{
  "by": "adam_inkling",
  "dead": true,
  "descendants": -1,
  "id": 88,
  "score": 1,
  "time": 1171907224,
  "title": "Project management alternative to basecamp - ticketing and version control too :)",
  "type": "story",
  "url": "http://unfuddle.com"
}
```

<h2>Users</h2>

Returns the current user's HakerNews profile. Only users that have public activity (comments or story submissions) on the site are available through the API.

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/user/{user-id}.json?print=pretty`

<h3>Path parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| user-id   | string | Required. The user's unique ID. Case-sensitive. |

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. 'pretty'- returns the data in a human-readable format. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data). |

<h3>Response</h3>

`HTTP Code: 200 - OK`

```
{
  "about": "string",
  "created": number,
  "delay": integer,
  "id": "string",
  "karma": number,
  "submitted": [
    integer,
    integer
  ]
}
```

|Parameter    | Type | Description |
| ------------- |-------------|--------|
id | string | Required. The user's unique ID. Case-sensitive.
delay | integer | Optional. Delay in minutes between a comment's creation and its visibility to other users. Max 10.
created | number | Required. Timestamp of the user creation, in [Unix Time](http://en.wikipedia.org/wiki/Unix_time).
karma | number | Required. The user's karma. Can be negative.
about | string | Optional. The user's self-description.
submitted | array[integer] | Optional. List of IDs of stories, polls and comments, that user posted.

<h3>Example</h3>

<h4>Request</h4>

`GET https://hacker-news.firebaseio.com/v0/user/myafka.json?print=pretty`
  
<h4>Response</h4>

`HTTP Code: 200 - OK`

```
{
  "about": "Test user for HackerNewsDocs",
  "created": 1596629617,
  "id": "myafka",
  "karma": 1
}
```

<h2>Max Item ID</h2>

Returns the current largest item ID. You can walk backwards from here to discover all items.

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. 'pretty'- returns the data in a human-readable format. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data). |

<h3>Response</h3>

```
HTTP Code: 200 - OK

integer
```

|Parameter    | Type | Description |
| ------------- |-------------|--------|
id | integer | Required. The current largest item ID.

<h3>Example</h3>

<h4>Request</h4>

`GET https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty`
  
<h4>Response</h4>

```
HTTP Code: 200 - OK

24051058
```

<h2>Top Stories</h2>

Returns the top of 500 recent stories posted on HakerNews (also contains jobs).

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. 'pretty'- returns the data in a human-readable format. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data). |

<h3>Response</h3>

`HTTP Code: 200 - OK`

```
[
    integer,
    integer,
    integer,
    integer,
    integer,
    ...
    integer
]
```

|Parameter    | Type | Description |
| ------------- |-------------|--------|
stories id | array[integer] | Required. Max 500 IDs.

<h3>Example</h3>

<h4>Request</h4>

`GET https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty`
  
<h4>Response</h4>

`HTTP Code: 200 - OK`

```
[
    24050651,
    24049428,
    24049593,
    24050691,
    24049349,
    ...
    24009672
]
```

<h2>New Stories</h2>

Returns the 500 newest stories posted on HakerNews (https://news.ycombinator.com/newest).

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. 'pretty'- returns the data in a human-readable format. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data). |

<h3>Response</h3>

`HTTP Code: 200 - OK`

```
[
    integer,
    integer,
    integer,
    integer,
    integer,
    ...
    integer
]
```

|Parameter    | Type | Description |
| ------------- |-------------|--------|
stories id | array[integer] | Required. Max 500 IDs.

<h3>Example</h3>

<h4>Request</h4>

`GET https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty`
  
<h4>Response</h4>

`HTTP Code: 200 - OK`

```
[
    24051158,
    24051138,
    24051134,
    24051125,
    24051071,
    ...
    24046636  
]
```

<h2>Best Stories</h2>

Returns the best stories posted on HakerNews (https://news.ycombinator.com/best).

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/besttories.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. 'pretty'- returns the data in a human-readable format. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data). |

<h3>Response</h3>

`HTTP Code: 200 - OK`

```
[
    integer,
    integer,
    integer,
    integer,
    integer,
    ...
    integer
]
```

|Parameter    | Type | Description |
| ------------- |-------------|--------|
stories id | array[integer] | Required. Max 500 IDs.

<h3>Example</h3>

<h4>Request</h4>

`GET https://hacker-news.firebaseio.com/v0/besttories.json?print=pretty`
  
<h4>Response</h4>

`HTTP Code: 200 - OK`

``` 
[
    24050651,
    24049428,
    24049593,
    24049349,
    24050837,
    ...
    24008501
]
```

<h2>Ask Stories</h2>

Returns the 200 ask stories posted on HakerNews (https://news.ycombinator.com/ask).

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/askstories.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. 'pretty'- returns the data in a human-readable format. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data). |

<h3>Response</h3>

`HTTP Code: 200 - OK`

``` 
[
    integer,
    integer,
    integer,
    integer,
    integer,
    ...
    integer
]
```

|Parameter    | Type | Description |
| ------------- |-------------|--------|
stories id | array[integer] | Required. Max 200 IDs.

<h3>Example</h3>

<h4>Request</h4>

`GET https://hacker-news.firebaseio.com/v0/askstories.json?print=pretty`
  
<h4>Response</h4>

`HTTP Code: 200 - OK`

``` 
[
    24051491,
    24038520,
    24050732,
    24047683,
    24038518,
    ...
    24029286
]
```

<h2>Show Stories</h2>

Returns the 200 show stories posted on HakerNews (https://news.ycombinator.com/show).
 
<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/showstories.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. 'pretty'- returns the data in a human-readable format. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data). |

<h3>Response</h3>

`HTTP Code: 200 - OK`

``` 
[
    integer,
    integer,
    integer,
    integer,
    integer,
    ...
    integer
]
```

|Parameter    | Type | Description |
| ------------- |-------------|--------|
stories id | array[integer]| Required. Max 200 IDs.

<h3>Example</h3>

<h4>Request</h4>

`GET https://hacker-news.firebaseio.com/v0/showstories.json?print=pretty`
  
<h4>Response</h4>

`HTTP Code: 200 - OK`

``` 
[
    24048786,
    24049421,
    24048508,
    24037118,
    24029002,
    ...
    24005615
]
```

<h2>Job Stories</h2>

Returns the 200 jobs posted on HakerNews (https://news.ycombinator.com/jobs).
 
<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. 'pretty'- returns the data in a human-readable format. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data). |

<h3>Response</h3>

`HTTP Code: 200 - OK`

``` 
[
    integer,
    integer,
    integer,
    integer,
    integer,
    ...
    integer
]
```

|Parameter    | Type | Description |
| ------------- |-------------|--------|
stories id | array[integer] | Required. Max 200 IDs.

<h3>Example</h3>

<h4>Request</h4>

`GET https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty`
  
<h4>Response</h4>

`HTTP Code: 200 - OK`

``` 
[
    24053023,
    24050427,
    24044432,
    24042289,
    24039626,
    ...
    23375443
]
```

<h2>Updates</h2>

Returns item IDs and users IDs where there were changes.

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/updates.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. 'pretty'- returns the data in a human-readable format. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data). |

<h3>Response</h3>

`HTTP Code: 200 - OK`

```
{
  "items": [
    integer,
    integer,
    integer,
    integer,
    integer,
    ...
    integer
  ],
  "profiles": [
    "string",
    "string",
    "string",
    "string",
    "string",
    ...
    "string"
  ]
}
```

|Parameter    | Type | Description |
| ------------- |-------------|--------|
items[] | array[integer] | Required. The list of HackerNews item IDs where there were changes.
profiles[] | array[string] | Required. The list of HackerNews users IDs where there were changes. User ID can only contain letters, digits, dashes and underscores, and could be between 2 and 15 characters long.

<h3>Example</h3>

<h4>Request</h4>

`GET https://hacker-news.firebaseio.com/v0/updates.json?print=pretty`
  
<h4>Response</h4>

`HTTP Code: 200 - OK`

```
{
  "items": [
    24053885,
    24053199,
    24053575,
    24051437,
    24051604,
    ...
    24044626
  ],
  "profiles": [
    "emiliobumachar",
    "kergonath",
    "Taek",
    "catacombs",
    "dlivingston",
    ...
    "mistersquid"
  ]
}
```
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



