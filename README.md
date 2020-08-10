# Overview

The HackerNews API is used for getting information from the site [HackerNews](https://news.ycombinator.com). The API was built using Firebase. 


* [Get started](#getting-started)

* Get to know [about site](#about-hacker-news) Hacker News

* Learn about API [methods](#methods)

* Read about other [use cases](#use-cases)


# Getting started

You can use this API to get information from the site https://news.ycombinator.com. For example, a list of the most popular stories or the title and URL of a story.

Examples in this guide are written in Python 3. You can use any programming language to work with the API.

## Step 1. The top stories

Let's find out what stories are in the top right now. To do this, we need the [Top Stories method](#top-stories). You don't need to set path parameters in this method.
 
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

## Step 2. The information about the item

The ID is a very important and useful entity that binds everything together. Using the ID, you can find the desired story. For example, let's see what is so special about the ID 24050651 story because it is so popular.

To do this, we need the [Item method](#item). In this method, you need to set ID as a path parameter.

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

## Step 3. The information about the user

To get data about a user, you need the [User method](#user). In this method, you need to set user ID.
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
Now we know that maxraz has good karma and he has many other stories. If you are interested, you can see what they are about using the method from Step 2.

<b>What's next</b>

* [Learn about API methods](#methods)

* [Read about other use cases](#use-cases)


# About Hacker News

Hacker News is a social news site focusing on computer science and entrepreneurship. 

The site has several items of content:

* story - post with a link to an interesting article, there are several subtypes:
  * ask - post with text for discussion
  * show - post with something that you've made
* job - thread where you can post job offers
* comment - self-explanatory
* poll - a survey with a set of answer options, each answer is a pollopt

The site has several collections of stories: 
* top stories (https://news.ycombinator.com/news) - top of the recent stories  
* newest stories (https://news.ycombinator.com/newest) - recently published stories 
* best stories (https://news.ycombinator.com/top)- best of the best stories 

# Methods

This section contains a description of HackerNews API. If you don't know anything about site HackerNews, at first read the article [About](#about-hacker-news).


| Method      | Description |
| ------------- |-------------|
| [item](#item) | Returns the information about the item (job, story, comment, poll or pollopt). |
| [user](#user) | Returns the current user's HakerNews profile. |
| [maxitem](#max-item-id) | Returns the current largest item ID. |
| [topstories](#top-stories) | Returns the top of recent stories posted on HakerNews. |
| [newstories](#new-stories) | Returns the newest stories posted on HakerNews. |
| [beststories](#best-stories) | Returns the best stories posted on HakerNews. |
| [askstories](#ask-stories) | Returns the ask stories posted on HakerNews. |
| [showstories](#show-stories) | Returns the show stories posted on HakerNews. |
| [jobstories](#job-stories) | Returns the latest jobs posted on HakerNews. |
| [updates](#updates) | Returns item IDs and users IDs where there were changes. |


## Item

Returns the information about the item (job, story, comment, poll or pollopt).

### HTTP request

`GET https://hacker-news.firebaseio.com/v0/item/{id}.json`

### Path parameters

|Parameter | Type | Description |
| ------------- |-------------|--------|
| id | integer | Required. The item's unique identifier. |

### Query parameters

Optional. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data).

### Response

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
| parent | integer | Optional. The item's parent. |||✔|||
| poll | integer | Optional. The pollopt's associated poll. |||||✔|
| kids | array[integer] | Optional. The IDs of the item's comments, in ranked display order. |✔|✔|✔|✔|✔|
| url | string | Optional. The URL. |✔|✔||||
| score | integer | Optional. The score for a story, or the votes for a pollopt. |✔|||✔|✔|
| title | string | Optional. The title of the story, poll or job.    |✔|✔||✔||
| parts | array[integer] | Optional. A list of related pollopts, in the display order.    ||||✔||
| descendants | integer | Optional. The total comment count.    |✔|||✔||

### Example

#### Request

  `GET https://hacker-news.firebaseio.com/v0/item/88.json`
  
#### Response

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

## User

Returns the current user's HakerNews profile. Only users that have public activity (comments or story submissions) on the site are available through the API.

### HTTP request

`GET https://hacker-news.firebaseio.com/v0/user/{user-id}.json`

### Path parameters

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| user-id   | string | Required. The user's unique ID. Case-sensitive. |

### Query parameters

Optional. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data).

### Response

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
created | number | Required. The timestamp of the user creation, in [Unix Time](http://en.wikipedia.org/wiki/Unix_time).
karma | number | Required. The user's karma. Can be negative.
about | string | Optional. The user's self-description.
submitted | array[integer] | Optional. List of IDs of stories, polls and comments, that user posted.

### Example

#### Request

`GET https://hacker-news.firebaseio.com/v0/user/myafka.json`
  
#### Response

`HTTP Code: 200 - OK`

```
{
  "about": "Test user for HackerNewsDocs",
  "created": 1596629617,
  "id": "myafka",
  "karma": 1
}
```

## Max Item ID

Returns the current largest item ID. You can walk backwards from here to discover all items.

### HTTP request

`GET https://hacker-news.firebaseio.com/v0/maxitem.json`

### Query parameters

Optional. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data).

### Response

```
HTTP Code: 200 - OK

integer
```

|Parameter    | Type | Description |
| ------------- |-------------|--------|
id | integer | Required. The current largest item ID.

### Example

#### Request

`GET https://hacker-news.firebaseio.com/v0/maxitem.json`
  
#### Response

```
HTTP Code: 200 - OK

24051058
```

## Top Stories

Returns the top of 500 recent stories posted on HakerNews (also contains jobs).

### HTTP request

`GET https://hacker-news.firebaseio.com/v0/topstories.json`

### Query parameters

Optional. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data).

### Response

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

### Example

#### Request

`GET https://hacker-news.firebaseio.com/v0/topstories.json`
  
#### Response

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

## New Stories

Returns the 500 newest stories posted on HakerNews (https://news.ycombinator.com/newest).

### HTTP request

`GET https://hacker-news.firebaseio.com/v0/newstories.json`

### Query parameters

Optional. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data).

### Response

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

### Example

#### Request

`GET https://hacker-news.firebaseio.com/v0/newstories.json`
  
#### Response

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

## Best Stories

Returns the best stories posted on HakerNews (https://news.ycombinator.com/best).

### HTTP request

`GET https://hacker-news.firebaseio.com/v0/besttories.json`

### Query parameters

Optional. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data).

### Response

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

### Example

#### Request

`GET https://hacker-news.firebaseio.com/v0/besttories.json`
  
#### Response

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

## Ask Stories

Returns the 200 ask stories posted on HakerNews (https://news.ycombinator.com/ask).

### HTTP request

`GET https://hacker-news.firebaseio.com/v0/askstories.json`

### Query parameters

Optional. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data).

### Response

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

### Example

#### Request

`GET https://hacker-news.firebaseio.com/v0/askstories.json`
  
#### Response

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

## Show Stories

Returns the 200 show stories posted on HakerNews (https://news.ycombinator.com/show).
 
### HTTP request

`GET https://hacker-news.firebaseio.com/v0/showstories.json`

### Query parameters

Optional. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data).

### Response

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

### Example

#### Request

`GET https://hacker-news.firebaseio.com/v0/showstories.json`
  
#### Response

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

## Job Stories

Returns the 200 jobs posted on HakerNews (https://news.ycombinator.com/jobs).
 
### HTTP request

`GET https://hacker-news.firebaseio.com/v0/jobstories.json`

### Query parameters

Optional. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data).

### Response

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

### Example

#### Request

`GET https://hacker-news.firebaseio.com/v0/jobstories.json`
  
#### Response

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

## Updates

Returns item IDs and users IDs where there were changes.

### HTTP request

`GET https://hacker-news.firebaseio.com/v0/updates.json`

### Query parameters

Optional. More in the [Firebase Docs](https://firebase.google.com/docs/database/rest/retrieve-data).

### Response

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
profiles[] | array[string] | Required. The list of HackerNews users IDs where there were changes. The user ID can only contain letters, digits, dashes and underscores, and could be between 2 and 15 characters long.

### Example

#### Request

`GET https://hacker-news.firebaseio.com/v0/updates.json`
  
#### Response

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
# Use cases

This section contains examples of API usage. The examples in this guide are written in Python 3. You can use any programming language to work with the API.

If you are a new to this API, we recommend starting with [Getting started](#getting-started).

## Fetch 50 stories

Imagine that you need to select 50 new stories. Since the [New Stories method](#new-stories) returns 500 stories, you will need to take additional steps.

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
  
## Sorted stories

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

Well done! The story "Why there’s so little left of the early internet" has the biggest score.

### Create a mobile app

Our API uses Firebase. Firebase serves as a database that changes in real-time and stores data in JSON. Any changes to the database are immediately synced between all clients or devices that use the same database. 

You can use Firebase SDK to create a mobile app for Android and iOS. To get started, visit the [Firebase setup instructions](https://firebase.google.com/docs/).

Here is an example of a [Swift app](https://github.com/timshim/Hackery).



