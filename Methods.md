<h1>Methods</h1>


| Method      | Description |
| ------------- |-------------|
| [items](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#Items) | Gets the information about the item (job, story, comment, poll or pollopt). |
| [users](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#Users) | Gets the current user's HakerNews profile. |
| [maxitem](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#max-item-id) | Gets the current largest item id. |
| [topstories](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#top-stories) | Gets the top stories posted on HakerNews. |
| [newstories](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#new-stories) | Gets the newest stories posted on HakerNews. |
| [beststories](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#bests-stories) | Gets the best stories posted on HakerNews. |
| [askstories](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#asks-stories) | Gets the top ask stories posted on HakerNews. |
| [showstories](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#shows-stories) | Gets the show stories posted on HakerNews. |
| [jobstories](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#job-stories) | Gets the latest jobs posted on HakerNews. |
| [updates](https://github.com/myafka/HackerNewsDocs/blob/master/Methods.md#updates) | Gets item ids and profile ids where there were changes. |


<h2>Items</h2>

Gets the information about the item (job, story, comment, poll or pollopt).

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty`

<h3>Path parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| id   | integer | Required. The item's unique id. |

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. defaul is pretty |

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
| id   | integer | Required. The item's unique id.|✔|✔|✔|✔|✔|
| deleted | boolean | Optional. true if the item is deleted.  |✔|✔|✔|✔|✔|
| type | string | Required. The type of item. One of "job", "story", "comment", "poll", or "pollopt".    |✔|✔|✔|✔|✔|
| by | string | Optional. The username of the item's author.    |✔|✔|✔|✔|✔|
| time | integer | Optional. Creation date of the item, in Unix Time.    |✔|✔|✔|✔|✔|
| text | string | Optional. The comment, story or poll text. HTML.    ||✔|✔|✔||
| dead | boolean | Optional. true if the item is dead. |✔|✔|✔|✔|✔|
| parent | integer | Optional. The comment's parent: either another comment or the relevant story.   |||✔||✔|
| poll | integer | Optional. The pollopt's associated poll. |||||✔|
| kids | array[integer] | Optional. The ids of the item's comments, in ranked display order. |✔|✔|✔|✔|✔|
| url | string | Optional. The URL of the story. |✔|✔||||
| score | integer | Optional. The story's score, or the votes for a pollopt. |✔|||✔|✔|
| title | string | Optional. The title of the story, poll or job. HTML.   |✔|✔||✔||
| parts | array[integer] | Optional. A list of related pollopts, in display order.    ||||✔||
| descendants | integer | Optional. In the case of stories or polls, the total comment count.    |✔|||✔||

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

Gets the current user's HakerNews profile. Only users that have public activity (comments or story submissions) on the site are available through the API.

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/user/{user-id}.json?print=pretty`

<h3>Path parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| user-id   | string | Required. The user's unique username. Case-sensitive. |

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. defaul is pretty |

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
id | string | Required. The user's unique username. Case-sensitive.
delay | integer | Optional. Delay in minutes between a comment's creation and its visibility to other users. Max 10.
created | number | Required. Creation date of the user, in [Unix Time](http://en.wikipedia.org/wiki/Unix_time).
karma | number | Required. The user's karma.
about | string | Optional. The user's self-description. HTML.
submitted | array[integer] | Optional. List of the user's stories, polls and comments.

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

Gets the current largest item id. You can walk backward from here to discover all items.

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. Defaul is pretty |

<h3>Response</h3>

```
HTTP Code: 200 - OK

integer
```

|Parameter    | Type | Description |
| ------------- |-------------|--------|
id | integer | Required. The current largest item id.

<h3>Example</h3>

<h4>Request</h4>

`GET https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty`
  
<h4>Response</h4>

```
HTTP Code: 200 - OK

24051058
```

<h2>Top Stories</h2>

Gets the top ask stories posted on HakerNews (also contains jobs). Up to 500.

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. Defaul is pretty |

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
stories id | array[integer] | Required. Max 500 id.

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

Up to 500 top stories (also contains jobs).

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. Defaul is pretty |

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
stories id | array[integer] | Required. Max 500 id.

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

Gets the best stories posted on HakerNews.

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/besttories.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. defaul is pretty |

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
stories id | array[integer] | Required. Max 500 id.

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

Up to 200 of the latest Ask stories

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/askstories.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. defaul is pretty |

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
stories id | array[integer] | Required. Max 200 id.

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

Gets the show stories posted on HakerNews. Up to 200.
 
<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/showstories.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. defaul is pretty |

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
stories id | array[integer]| Required. Max 200 id.

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

Gets the latest jobs posted on HakerNews. Up to 200.
 
<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. defaul is pretty |

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
stories id | array[integer] | Required. Max 200 id.

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

<h2>Updeites</h2>

Gets item ids and profile ids where there were changes.

<h3>HTTP request</h3>

`GET https://hacker-news.firebaseio.com/v0/updates.json?print=pretty`

<h3>Query parameters</h3>

|Parameter    | Type | Description |
| ------------- |-------------|--------|
| print   | string | Optional. Defaul is pretty |

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
items[] | array[integer] | Required. The list of HackerNews item ids where there were changes.
profiles[] | array[string] | Required. The list of HackerNews profiles ids where there were changes.

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
