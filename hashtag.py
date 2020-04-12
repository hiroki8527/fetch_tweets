#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask, jsonify, request
import tweepy
from config import base_setting

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
@app.route('/hashtags/<string:keyword>', methods=["GET"])

def get_tweets(keyword):
    keyword = '#{} -filter:retweets'.format(keyword)
    DEFAULT_LIMIT_NUMBER = 30
    limit = request.args.get('limit')
    if not limit:
        limit = DEFAULT_LIMIT_NUMBER

    auth = tweepy.OAuthHandler(base_setting.CONSUMER_KEY, base_setting.CONSUMER_SECRET)
    auth.set_access_token(base_setting.ACCESS_TOKEN, base_setting.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth ,wait_on_rate_limit = True)
    result = []
    for status in api.search(q = keyword, count = limit):
        status_json = status._json
        user_status = status_json["user"]
        tweet_info = {
            "account":
                {
                "fullname": user_status["name"],
                "href": "/" + user_status["screen_name"],
                 "id": user_status["id"]
                 },
            "date": get_date(status_json["created_at"]),
            "hashtags": get_hashtags(status_json["entities"]["hashtags"]),
            "likes": status_json["favorite_count"],
            "replies": 0,
            "retweets": status_json["retweet_count"],
            "text": status_json["text"]
            }
        result.append(tweet_info)
    return jsonify(result)

def get_hashtags(hashtags):
    if len(hashtags) == 0:
        hashtag = None
    else:
        hashtag = ["#" + hashtag["text"] for hashtag in hashtags]
    return hashtag

def get_date(date):
    splited_data = date.split()
    month = splited_data[1]
    day = splited_data[2]
    time = splited_data[3]
    year = splited_data[5]
    splited_time = time.split(":")
    hours = splited_time[0]
    minutes = splited_time[0]
    meridian = "PM" if int(hours) > 11 else "AM"
    return '{}:{} {} - {} {}'.format(hours, minutes, meridian, month, year)
