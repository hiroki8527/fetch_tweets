import sys
sys.path.append('../script')
from api import app
from flask import json


def test_get_tweets_by_screen_name():
    screen_name = "realdonaldtrump"
    limit = 5
    response = app.test_client().get(
        "/users/{}?limit={}".format(screen_name, limit),
        content_type = "application/json",
    )
    data = json.loads(response.get_data(as_text = True))

    assert response.status_code == 200
    for status in data:
        assert status["account"]["href"][1:] == screen_name


def test_get_tweets_by_screen_name():
    screen_name = "AbeShinzo"
    limit = 100
    response = app.test_client().get(
        "/users/{}?limit={}".format(screen_name, limit),
        content_type = "application/json",
    )
    data = json.loads(response.get_data(as_text = True))

    assert response.status_code == 200
    for status in data:
        assert status["account"]["href"][1:] == screen_name
