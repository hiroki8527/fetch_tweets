#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import tweepy
import sys
sys.path.append('../')
from config import base_setting

def parse_hashtags(hashtags):
    if len(hashtags) == 0:
        hashtag = None
    else:
        hashtag = ["#" + hashtag["text"] for hashtag in hashtags]
    return hashtag

def parse_date(date):
    if len(date) == 0:
        return None
    else:
        splited_data = date.split()
        month = splited_data[1]
        day = splited_data[2]
        time = splited_data[3]
        year = splited_data[5]
        splited_time = time.split(":")
        hours = splited_time[0]
        minutes = splited_time[1]
        meridian = "PM" if int(hours) > 11 else "AM"
        return "{}:{} {} - {} {}".format(hours, minutes, meridian, month, year)

def set_tweepy_api():
    auth = tweepy.OAuthHandler(base_setting.CONSUMER_KEY, base_setting.CONSUMER_SECRET)
    auth.set_access_token(base_setting.ACCESS_TOKEN, base_setting.ACCESS_TOKEN_SECRET)
    return tweepy.API(auth, wait_on_rate_limit = True)

def generate_json_about_tweet(status):
    status_json = status._json
    user_status = status_json["user"]
    generated_json = {
        "account":
            {
            "fullname": user_status["name"],
            "href": "/" + user_status["screen_name"],
             "id": user_status["id"]
             },
        "date": parse_date(status_json["created_at"]),
        "hashtags": parse_hashtags(status_json["entities"]["hashtags"]),
        "likes": status_json["favorite_count"],
        "replies": 0,
        "retweets": status_json["retweet_count"],
        "text": status_json["full_text"]
        }
    return generated_json

def set_limit(limit, default):
    if not limit:
        limit = default
    return limit
