import sys
sys.path.append('../script')
from api import app
from flask import json

def test_get_tweets_by_japanese_keyword():
    keyword = "家にいよう"
    given_hashtag = "#" + keyword
    limit = 10
    response = app.test_client().get(
        "/hashtags/{}?limit={}".format(keyword, limit),
        content_type = "application/json",
    )
    data = json.loads(response.get_data(as_text = True))

    assert response.status_code == 200
    for status in data:
        hashtag_exists = None
        for hashtag in status["hashtags"]:
            if given_hashtag.lower() == hashtag.lower():
                hashtag_exists = True
                break
        assert hashtag_exists == True

def test_get_tweets_by_english_keyword():
    keyword = "stayhome"
    given_hashtag = "#" + keyword
    limit = 50
    response = app.test_client().get(
        "/hashtags/{}?limit={}".format(keyword, limit),
        content_type = "application/json",
    )
    data = json.loads(response.get_data(as_text = True))

    assert response.status_code == 200
    for status in data:
        hashtag_exists = None
        for hashtag in status["hashtags"]:
            if given_hashtag.lower() == hashtag.lower():
                hashtag_exists = True
                break
        assert hashtag_exists == True
