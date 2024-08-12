import os
import tweepy

# Redirect URI
redirect_uri = os.environ['redirect_uri']

# Client ID and Secret
client_id = os.environ['client_id']
client_secret = os.environ['client_secret']

# Access Token and Secret
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

# Consumer Key and Secret 
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']

# Truth Terminal Twitter ID
truth_terminal_twitter_id = os.environ['truth_terminal_twitter_id']





# 3-legged OAuth
# -> Uncomment the below code, should the access_token and access_token_secret ever become invalid

# oauth1_user_handler = tweepy.OAuth1UserHandler(
#     consumer_key, consumer_secret,
#     callback=redirect_uri
# )

# print("Step 1: Open this URL and approve: " + oauth1_user_handler.get_authorization_url())
# print("Step 2: Copy the the oauth_verifier URL param from the redirect URL")

# oauth_verifier = input("Step 3: Paste the oauth_verifier here and press enter: ")

# access_token, access_token_secret = oauth1_user_handler.get_access_token(
#     oauth_verifier
# )

# print("access_token: ", access_token, "\n", "access_token_secret: ", access_token_secret)



# #
# # @truth_terminal's keys, after doing the above 3-legged dance. these can be found in Replit's secrets tab if they need changing in the future
# #
# access_token = os.environ['access_token']
# access_token_secret = os.environ['access_token_secret']


# client = tweepy.Client(
#     consumer_key=consumer_key,
#     consumer_secret=consumer_secret,
#     access_token=access_token,
#     access_token_secret=access_token_secret
# )





#
# OAuth 2.0 Client
#

# ###############
# UNCOMMENT AND RUN THIS SECTION FIRST

# oauth2_user_handler = tweepy.OAuth2UserHandler(
#     client_id=client_id,
#     redirect_uri=redirect_uri,
#     scope=[
#         "tweet.read",
#         "tweet.write",
#         "tweet.moderate.write", # Hide and unhide replies to your Tweets
#         "users.read",
#         "follows.read",
#         "follows.write", # Follow and unfollow people for you
#         "offline.access", # Stay connected to your account until you revoke access
#         "space.read",
#         "mute.read",
#         "mute.write", # Mute and unmute accounts for you
#         "like.read",
#         "like.write",
#         "list.read",
#         "list.write", # Create and manage Lists for you
#         "block.read",
#         "block.write", # Block and unblock accounts for you
#         "bookmark.read",
#         "bookmark.write" # Bookmark and remove Bookmarks from Tweets
#     ],
#     client_secret=client_secret
# )

# print("Step 1: Open this URL and approve: " + oauth2_user_handler.get_authorization_url() + "\n")

# print("Step 2: Copy the authorization response URL" + "\n")

# oauth2_authorization_url = input("Step 3: Paste authorization response URL here and press enter: ")

# token = oauth2_user_handler.fetch_token(
#     oauth2_authorization_url
# )
# print()
# print("-- Received: ", token, "\n")

# print("Step 4: set 'oauth2_offline_full_access_token' in Secrets to: ", token['access_token'])

################

################
# UNCOMMENT AND RUN THIS SECTION SECOND 
# (after 'oauth2_offline_full_access_token' is set in Secrets)

oauth2_offline_full_access_token = os.environ['oauth2_offline_full_access_token']

client = tweepy.Client(oauth2_offline_full_access_token)

# Create a v1 API client for media uploads
# TODO: TEMP use const_labs for now
const_labs_access_token = os.environ['const_labs_access_token']
const_labs_access_token_secret = os.environ['const_labs_access_token_secret']

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
     const_labs_access_token, const_labs_access_token_secret
)
api = tweepy.API(auth)
#
################





# # Get Tweets

# # This endpoint/method returns a variety of information about the Tweet(s)
# # specified by the requested ID or list of IDs

# tweet_ids = [1808784757129687539]

# # By default, only the ID and text fields of each Tweet will be returned
# # Additional fields can be retrieved using the tweet_fields parameter
# response = client.get_tweets(tweet_ids, tweet_fields=["created_at"])

# for tweet in response.data:
#     print(tweet.id, tweet.created_at)





# # # Get User's Tweets

# # # This endpoint/method returns Tweets composed by a single user, specified by
# # # the requested user ID

# tweets = client.get_users_tweets(truth_terminal_twitter_id)
# print(tweets)

# # By default, only the ID and text fields of each Tweet will be returned
# for tweet in tweets.data:
#     print(tweet.id)
#     print(tweet.text)

# # By default, the 10 most recent Tweets will be returned
# # You can retrieve up to 100 Tweets by specifying max_results
# response = client.get_users_tweets(user_id, max_results=10)





# Get User's Mentions

# This endpoint/method returns Tweets mentioning a single user specified by the
# requested user ID

# response = client.get_users_mentions(truth_terminal_twitter_id)

# # By default, only the ID and text fields of each Tweet will be returned
# for tweet in response.data:
#     print(tweet.id)
#     print(tweet.text)

# print()



# # Search Recent Tweets
# # This endpoint/method returns Tweets from the last seven days

# response = clientUserContext.search_recent_tweets("ConstellateLabs")
# # The method returns a Response object, a named tuple with data, includes,
# # errors, and meta fields
# print(response.meta)

# # In this case, the data field of the Response returned is a list of Tweet
# # objects
# tweets = response.data

# # Each Tweet object has default ID and text fields
# for tweet in tweets:
#     print(tweet.id)
#     print(tweet.text)





# # Post a Hello world! Tweet
# response = client.create_tweet(
#     text="Hello world! Paging @andyayrey",
#     user_auth=False
# )
# print(f"https://twitter.com/user/status/{response.data['id']}")

# # Post a reply tweet
# response = client.create_tweet(
#     text="Is this thing #on?",
#     in_reply_to_tweet_id=1820682199051456677,
#     user_auth=False
# )
# print(f"https://twitter.com/user/status/{response.data['id']}")

# # Post a too-long Hello world! Tweet
# response = client.create_tweet(
#     text="Hello world! Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas mi ante, convallis eu pretium pharetra, venenatis ut lacus. Nullam euismod vulputate placerat. Proin laoreet dapibus molestie. Vestibulum finibus ipsum tellus, nec ornare odio porta at. Cras id ante a tellus ornare consequat. Maecenas eu augue augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas placerat magna eget nulla finibus, ut sagittis dui aliquam. Nam finibus aliquet justo, in maximus leo pharetra ac. Vestibulum vitae efficitur elit, vel dignissim dui. Aenean tortor eros, aliquet nec feugiat id, tempus ac felis. Quisque vel commodo nunc. In condimentum massa nec quam lobortis blandit. Suspendisse placerat placerat justo sed suscipit. Phasellus vehicula egestas nibh vel tempor. Praesent quis auctor augue, id pellentesque augue. Donec luctus porta ullamcorper. Cras id feugiat purus, at venenatis purus. Etiam finibus neque sed dictum tincidunt. Donec placerat pharetra ligula, venenatis volutpat velit. In vitae elit sem. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum fermentum justo in quam euismod, at malesuada urna semper. Nulla tristique dolor quis luctus sagittis. Duis eget sapien risus.", 
#     user_auth=False
# )
# print(f"https://twitter.com/user/status/{response.data['id']}")




# Upload an image
# upload_response = api.media_upload("Constellate Logo.png")
# print(upload_response)

# Post a Hello world! Tweet with an image
# response = client.create_tweet(
#     text="Hello world!",
#     media_ids=[upload_response['media_id']],
#     user_auth=False
# )
# print(f"https://twitter.com/user/status/{response.data['id']}")