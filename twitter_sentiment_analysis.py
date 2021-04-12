from textblob import TextBlob
import tweepy
import sys

# Personal Keys from Twitter account
# Access your account to get the values
api_key = ''
api_key_secret = ''
access_token = ''
access_token_secret = ''

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = 'Batman'
tweet_amount = 250

tweets = tweepy.Cursor(api.search, q=search_term, lang='pt').items(tweet_amount)

polarity = 0
positive = 0
neutral = 0
negative = 0

# Filtrating the data
for tweet in tweets:
    final_text = tweet.text.replace('RT', '')
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position+2:]
    if final_text.startswith('@'):
        position = final_text.index(' ')
        final_text = final_text[position+2:]
    analysis = TextBlob(final_text)
    tweet_polarity = analysis.polarity

    # Counting number of positive/neutral/negative tweets
    if tweet_polarity > 0:
        positive += 1
    elif tweet_polarity < 0:
        negative += 1
    else:
        neutral += 1

    polarity += analysis.polarity

print(polarity)
print(f'Amount of positive tweets: {positive}')
print(f'Amount of neutral tweets: {neutral}')
print(f'Amount of negative tweets: {negative}')
