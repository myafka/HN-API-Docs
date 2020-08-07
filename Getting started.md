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
