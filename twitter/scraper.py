import tweepy

# Twitter API credentials (replace with your actual credentials)
API_KEY = "hfDIubvS0ktIS4F7u8adh3Nnh"
API_SECRET_KEY = "fkTXtsPEt4pdTb4AapUwvdb96oAJQqkYkBOQQYCrW1b6YbRH9E"
ACCESS_TOKEN = "1476214697598857217-wMJKSuMrUAglccWGosYmAPB1qm9XRx"
ACCESS_TOKEN_SECRET = "cI89QimxM7U8lAwgUzOPburF92kseVwGFt6b1LX12WA6Y"

# # Authenticate to Twitter
# auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

def search_and_save_tweets(hashtag, username, output_file):
    """
    Searches for tweets with a specific hashtag and checks if the user follows a specific account.
    Saves qualifying tweets to a file.

    :param hashtag: The hashtag to search for (e.g., "#PlumPick").
    :param username: The username to check if users follow (e.g., "plums_ai").
    :param output_file: The file to save the tweet texts to.
    """
    tweets_list = []

    try:
        # Search for tweets with the specified hashtag
        for tweet in tweepy.Cursor(api.search_tweets, q=hashtag, lang="en").items(10):
            try:
                # Check if the tweet's user follows the specified account
                friendship = api.get_friendship(source_screen_name=tweet.user.screen_name, target_screen_name=username)
                if friendship[0].following:
                    tweets_list.append(tweet.text)
            except tweepy.TweepyException as e:
                print(f"Error checking friendship for {tweet.user.screen_name}: {e}")

        # Save the tweets to a file
        with open(output_file, 'w', encoding='utf-8') as f:
            for tweet_text in tweets_list:
                f.write(tweet_text + '\n')

        print(f"Saved {len(tweets_list)} tweets to {output_file}")

    except tweepy.TweepyException as e:
        print(f"Error during tweet search: {e}")

# Example usage
# search_and_save_tweets("#PlumPick", "plums_ai", "twitter/twitterplumpick_tweets.txt")


# # Authenticate and create the API client
# auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

# response = client.create_tweet

client = tweepy.Client(consumer_key=API_KEY,
                       consumer_secret=API_SECRET_KEY,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)

response = client.create_tweet(text="Testing X API")