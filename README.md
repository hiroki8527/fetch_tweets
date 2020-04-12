# fetch-tweets
## Setup
- This API is created with Python and Flask
- pytest is used for testing Flask application

### Prerequisites
- Python 3.x

### Install Flask and pytest
```bash
$ pip install Flask
$ pip install pytest
```

### Run API
Open console window
```bash
$ cd script
$ ls
__pycache__  api.py  common.py
$  FLASK_APP=api.py flask run
* Serving Flask app "api"
* Running on http://<your_localhost>/ (Press CTRL+C to quit)
```

### Send HTTP request using curl
Open another console window

- [1] Get the list of tweets with the given hashtag
```bash
$ curl -H "Accept: application/json" -X GET http://127.0.0.1:5000/hashtags/[keyword]>?limit=[limit]
```
You can choose [keyword] and [limit].

```bash
### (example1)
$ curl -H "Accept: application/json" -X GET http://<your_localhost>/hashtags/python?limit=10
### (example2)
$ curl -H "Accept: application/json" -X GET http://<your_localhost>/hashtags/stayhome?limit=30
```
- [2] Get the list of tweets that the user has on his feed

```bash
$ curl -H "Accept: application/json" -X GET http://<your_localhost>/users/[screen_name]?limit=[limit]
```
You can choose [screen_name] and [limit].

screen_name is @xxxxxxx in twitter.
So, if you want to Get the list of tweets of [Donald J. Trump](https://twitter.com/realdonaldtrump).
You would send HTTP request like this.
```bash
### (example)
$ curl -H "Accept: application/json" -X GET http://<your_localhost>/users/realdonaldtrump?limit=10
```
