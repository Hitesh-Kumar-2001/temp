import tweepy
import data_retriever
file_name = 'image.jpeg'
status = "you can search the artist here- https://ascii2d.net/ #waifus #animegirls #cuteanime #anime"
keys = data_retriever.get_keys()
apiKey = keys[0]
apikeySecret = keys[1]
accessToken = keys[2]
accessTokenSecret = keys[3]


oauth = tweepy.OAuthHandler(apiKey, apikeySecret)
oauth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(oauth)


def upload_media():
    media = api.media_upload(file_name)
    api.update_status(status,media_ids=[media.media_id_string])
    return 0

def auto_follow_back():
    for follower in tweepy.Cursor(api.get_followers).items():
        follower.follow()



# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")

