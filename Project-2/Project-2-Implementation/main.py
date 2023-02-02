import pymongo
from textblob import TextBlob
import numpy as np
import re
import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
reddit_db_con = my_client["redditdatabase"]
reddit_db_collection = reddit_db_con["redditcomments"]
twitter_db_con = my_client["twitterdatabase"]
twitter_db_collection = twitter_db_con["twitter"]
youtube_db_con = my_client["youtubedatabase"]
youtube_db_collection = youtube_db_con["youtube"]


global positive1
positive1 = 0
global negative1
negative1 = 0
global neutral1
neutral1 = 0
global positive2
positive2 = 0
global negative2
negative2 = 0
global neutral2
neutral2 = 0
global positive3
positive3 = 0
global negative3
negative3 = 0
global neutral3
neutral3 = 0



def clean_tweet(text_to_be_analyzed):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(#[A-Za-z0-9]+)", " ", str(text_to_be_analyzed)).split())


def twitter_data_analysis(text_to_be_analyzed):
    global positive1, neutral1, negative1
    analysis = TextBlob(clean_tweet(text_to_be_analyzed))

    if analysis.sentiment.polarity > 0.00:
        positive1 += 1
    elif analysis.sentiment.polarity == 0.00:
        neutral1 += 1
    elif analysis.sentiment.polarity < 0.00:
        negative1 += 1


def youtube_data_analysis(text_to_be_analyzed):
    global positive2, neutral2, negative2
    analysis = TextBlob(clean_tweet(text_to_be_analyzed))

    if analysis.sentiment.polarity > 0.00:
        positive2 += 1
    elif analysis.sentiment.polarity == 0.00:
        neutral2 += 1
    elif analysis.sentiment.polarity < 0.00:
        negative2 += 1

def reddit_data_analysis(text_to_be_analyzed):
    global positive3, neutral3, negative3
    analysis = TextBlob(clean_tweet(text_to_be_analyzed))
    if analysis.sentiment.polarity > 0.00:
        positive3 += 1
    elif analysis.sentiment.polarity == 0.00:
        neutral3 += 1
    elif analysis.sentiment.polarity < 0.00:
        negative3 += 1


def result():
    twitter_count = 0
    print("Waiting for analyzing twitter posts")
    for tweet in twitter_db_collection.find():
        twitter_count += 1
        np.array([twitter_data_analysis(tweet)])
        if twitter_count == 235197:
            break 
    print("--------------------------------------------------")
    print("Twitter positive posts count:", positive1)
    print("Twitter neutral posts count:", neutral1)
    print("Twitter negative posts count:", negative1)
    print("--------------------------------------------------")
    twitter_values = [positive1, neutral1, negative1]
    youtube_count = 0
    print("Waiting for analyzing youtube posts")
    for comment in youtube_db_collection.find():
        youtube_count += 1
        np.array([youtube_data_analysis(comment)])
        if youtube_count == 262312:
            break
    print("--------------------------------------------------")
    print("Youtube positive posts count:", positive2)
    print("Youtube neutral posts count:", neutral2)
    print("Youtube negative posts count:", negative2)
    print("--------------------------------------------------")
    youtube_values = [positive2, neutral2, negative2]
    reddit_count = 0
    print("Waiting for analyzing reddit posts from subreddit r/politics")
    for post in reddit_db_collection.find():
        reddit_count += 1
        np.array([reddit_data_analysis(post)])
        if reddit_count == 66603:
            break
    print("--------------------------------------------")
    print("Reddit positive posts count:", positive3)
    print("Reddit neutral posts count:", neutral3)
    print("Reddit negative posts count:", negative3)
    print("--------------------------------------------")
    reddit_values = [positive3, neutral3, negative3]
    return [twitter_values, youtube_values, reddit_values]


print("Final output results: \n", result())


