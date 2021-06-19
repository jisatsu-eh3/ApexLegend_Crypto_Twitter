import tweepy
import random
import config

def getQuote(rnint):
    with open('quotes.txt') as f:
        lines = f.readlines()

    count = 0
    # Strips the newline character
    quotes = []
    for line in lines:
        count += 1
        if line != '\n':
            quotes.append(line)

    print(quotes[rnint])
    return quotes[rnint]

def twitterPost(post):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(config.tweepy_secret, config.tweepy_token)
    auth.set_access_token(config.set_access_token, config.set_access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    # Create a tweet
    api.update_status(post)

def combinePost(post, hashtags):
    post = post + hashtags
    return post

#Hashtag string to add
hashtags = '#Apexlegend #ApexPredator #Crypto'

rm_int = random.randint(0, 133)
quotes = getQuote(rm_int)
post = combinePost(quotes, hashtags)
print(post)
twitterPost(post)
