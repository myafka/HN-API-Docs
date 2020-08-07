<h1>Methods</h1>


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
