import requests 
from bs4 import BeautifulSoup
import time
import os

def getBurrito(): 
    # URL of Chipotle's twitter feed
    url='https://twitter.com/ChipotleTweets?lang=en'

    # Retry every 5 seconds until found
    while True:
        resp=requests.get(url) 

        # http_respone 200 means OK status 
        if resp.status_code==200:  
            # Find first tweet of stream of tweets
            soup=BeautifulSoup(resp.text,'html.parser')      
            l=soup.find("ol",{"class":"stream-items"}) 

            # Get timestamp from tweet
            tweet_timestamp = l.find(class_="_timestamp")
            timestamp = int(tweet_timestamp['data-time'])

            # Check if tweet is less than a minute old
            if newTweet(timestamp):
                # If there is a new tweet, read the text and split the words into a list
                tweet = l.find(class_="tweet-text")
                tweet_text = tweet.text
                words = tweet_text.lower().split()

                # If the word "text" appears in the tweet, we can likely find the code
                if "text" in words:
                    text_index = words.index("text")

                    # Code is probably the word after "text"
                    code = words[text_index+1].upper()

                    # Call applescript to send text to Chipotle
                    os.system('osascript sendMessage.applescript "'+ code +'"')
                    break

        else: 
            print("Error") 
        
        # Sleep for 5 seconds so it doesn't constantly make requests
        time.sleep(5)

def newTweet(timestamp):
    return abs(time.time()-timestamp) < 60

getBurrito()