#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask, jsonify, request
import common

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/hashtags/<string:keyword>", methods=["GET"])
def get_tweets_by_keyword(keyword):
    hashtag = "#{} -filter:retweets".format(keyword)
    DEFAULT_LIMIT_NUMBER = 30
    limit = common.set_limit(request.args.get("limit"), DEFAULT_LIMIT_NUMBER)
    api = common.set_tweepy_api()
    result = []
    for status in api.search(q = hashtag, count = limit, tweet_mode = "extended"):
        result.append(common.generate_json_about_tweet(status))
    return jsonify(result)

@app.route("/users/<string:screen_name>", methods=["GET"])
def get_tweets_by_screen_name(screen_name):
    DEFAULT_LIMIT_NUMBER = 30
    limit = common.set_limit(request.args.get("limit"), DEFAULT_LIMIT_NUMBER)
    api = common.set_tweepy_api()
    result = []
    for status in api.user_timeline(screen_name = screen_name, count = limit, tweet_mode = "extended"):
        result.append(common.generate_json_about_tweet(status))
    return jsonify(result)
