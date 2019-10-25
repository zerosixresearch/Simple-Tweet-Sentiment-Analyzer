import streamlit as st
import tweepy
import json
import yaml
import operator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

with open("config.yml", "r") as ymlfile:
        config = yaml.load(ymlfile, Loader=yaml.SafeLoader)
        
auth = tweepy.OAuthHandler(config['CONSUMER_KEY'], config['CONSUMER_SECRET']) 
auth.set_access_token(config['ACCESS_TOKEN'], config['ACCESS_TOKEN_SECRET'])

st.header("Twitter Streamer and Sentiment Analysis")

st.write("This web application gets tweets from a hashtag and analyses text sentiment.")

t = st.text_input("Enter a hastag to stream tweets")

start = st.button("Get Tweets")

analyser = SentimentIntensityAnalyzer()

class StreamListener(tweepy.StreamListener):
    
    def on_status(self, status):
        if hasattr(status, "retweeted_status"):
            pass
        else:
            try:
                text = status.extended_tweet["full_text"]
                score = analyser.polarity_scores(text)
                st.write(text)
                m = max(score.items(), key=operator.itemgetter(1))[0]
                if m == 'neg':
                    st.error("The sentiment is: {}".format(str(score)))
                elif m == 'neu':
                    st.warning("The sentiment is: {}".format(str(score)))
                elif m == 'pos':
                    st.success("The sentiment is: {}".format(str(score)))
                else:
                    st.info("The sentiment is: {}".format(str(score)))
            except AttributeError:
                text = status.text
                score = analyser.polarity_scores(text)
                st.write(text)
                m = max(score.items(), key=operator.itemgetter(1))[0]
                if m == 'neg':
                    st.error("The sentiment is: {}".format(str(score)))
                elif m == 'neu':
                    st.warning("The sentiment is: {}".format(str(score)))
                elif m == 'pos':
                    st.success("The sentiment is: {}".format(str(score)))
                else:
                    st.info("The sentiment is: {}".format(str(score)))
        
def stream_tweets(tag):
    listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True, wait_on_rate_limit_notify=True))
    streamer = tweepy.Stream(auth=auth, listener=listener, tweet_mode='extended')
    query = [str(tag)]
    streamer.filter(track=query, languages=["en"])
    
if start:
    stream_tweets(str(t))