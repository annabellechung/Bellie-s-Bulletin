import os
import tweepy
import time

# The following are empty for safety reasons
API_Key = 
API_Key_Secret = 
Bearer_Token = 
Access_Token = 
Access_Token_Secret = 
Clinet_Secret = 

tweeted_messages = set()


def create_api():
    auth = tweepy.OAuthHandler('API_Key', 'API_Key_Secret')
    auth.set_access_token('Access_Token', 'Access_Token_Secret')

    return tweepy.API(auth)


# Posts a tweet out of the list of messages every 3 hours
def tweet(api: tweepy.API, message: str):
    if message in tweeted_messages:
        print(f"Skipping message: {message} (already tweeted)")
        return

        api.update_status(message)
        tweeted_messages.add(message)
        print(f"Tweeted message: {message}")

        time.sleep(3 * 60 * 60)

        api.update_status(message)


# The list of messages that can be outputted
messages = [
    
# messages were here

if __name__ == '__main__':
    api = create_api()
    tweeted_messages = set()
    print(’success!’)
