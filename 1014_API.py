#coding: UTF-8
from requests_oauthlib import OAuth1Session
import json
import os

#各情報をapp.twitterのアプリから持ってくる

CONSUMER_KEY=os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET=os.environ['TWITTER_CONSUMER_SECRET']
ACCESS_TOKEN=os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_TOKEN_SECRET=os.environ['TWITTER_ACCESS_TOKEN_SECRET']

##タイムラインに追加
#params = {'status': 'Hello, World!'}
#req = twitter.post('https://api.twitter.com/1.1/statuses/update.json',params = params)

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

params = {}
#タイムラインを取得
req = twitter.get('https://api.twitter.com/1.1/statuses/home_timeline.json', params = params)

timeline = json.loads(req.text)

for tweet in timeline:
  print(tweet['text'])
  print(tweet['favorite_count'])
