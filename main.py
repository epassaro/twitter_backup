import os
import twitter

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN_KEY = os.environ['ACCESS_TOKEN_KEY']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

print(CONSUMER_KEY[-5:])
print(CONSUMER_SECRET[-5:])
print(ACCESS_TOKEN_KEY[-5:])
print(ACCESS_TOKEN_SECRET[-5:])

api = twitter.Api(consumer_key=CONSUMER_SECRET,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)

friends = api.GetFriends(user_id='epassaro')
friends_df = pd.DataFrame(friends)
friends_df.to_csv('friends.csv')