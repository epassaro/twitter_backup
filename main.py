import os
import twitter
import pandas as pd

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN_KEY = os.environ['ACCESS_TOKEN_KEY']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']


if __name__ == "__main__":

    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN_KEY,
                      access_token_secret=ACCESS_TOKEN_SECRET)

    friends = api.GetFriends(user_id='epassaro')
    friends = [ f.AsDict() for f in friends ]
    friends_df = pd.DataFrame.from_records(friends)
    friends_df.to_csv('epassaros_friends.csv', index=False)