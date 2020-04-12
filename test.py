#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json, config #標準のjsonモジュールとconfig.pyの読み込み
# from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み
#
# CK = config.CONSUMER_KEY
# CS = config.CONSUMER_SECRET
# AT = config.ACCESS_TOKEN
# ATS = config.ACCESS_TOKEN_SECRET
# twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理
#
# url = "https://api.twitter.com/1.1/statuses/user_timeline.json" #タイムライン取得エンドポイント
#
# params ={'count' : 5} #取得数
# res = twitter.get(url, params = params)
#
# if res.status_code == 200: #正常通信出来た場合
#     timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
#     for line in timelines: #タイムラインリストをループ処理
#         print(line['user']['name']+'::'+line['text'])
#         print(line['created_at'])
#         print('*******************************************')
# else: #正常通信出来なかった場合
#     print("Failed: %d" % res.status_code)



##################################################################
import tweepy
limit= 4
keyword = "CcC6vw"
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth ,wait_on_rate_limit = True)
status = api.user_timeline(screen_name=keyword, count=limit)

def get_hashtags(json_hashtags):
    if len(json_hashtags) == 0:
        hashtag = None
    else:
        hashtag = ["#" + tag["text"] for tag in json_hashtags]
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

box = []
for s in status:
    a = {
        "account":
            {
            "fullname": s.user._json["name"],
            "href": "/" + s.user._json["screen_name"],
             "id": s.user._json["id"]
             },
        "date": get_date(s._json["created_at"]),
        "hashtags": get_hashtags(s._json["entities"]["hashtags"]),
        "likes": s._json["favorite_count"],
        "replies": 13,
        "retweets": s._json["retweet_count"],
        "text": s._json["text"]
        }
    box.append(a)
    box.append("〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜")

print(box)
# for s in status:
#     #見映えのため区切る
#     print('-------------------------------------------')
#     #ユーザ名表示
#     print('name:' + s.user.name)
#     #内容表示
#     print(s)
#     print('-------------------------------------------')


    ###################################################################################################
# import tweepy
# CONSUMER_KEY = config.CONSUMER_KEY
# CONSUMER_SECRET = config.CONSUMER_SECRET
# ACCESS_TOKEN = config.ACCESS_TOKEN
# ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET
#
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#
# class Listener(tweepy.StreamListener):
#     """ Handles tweets received from the stream. """
#
#     def on_status(self, status):
#         """ Prints tweet and hashtags """
#         print('------------------------------')
#         print(status.text)
#         for hashtag in status.entities['hashtags']:
#             print(hashtag['text']),
#         print("")
#         return True
#
#     def on_error(self, status_code):
#         print('Got an error with status code: ' + str(status_code))
#         return True
#
#     def on_timeout(self):
#         print('Timeout...')
#         return True
#
# listener = Listener()
# stream = tweepy.Stream(auth, listener)
# stream.filter(track=['#StayHome'])
