from DriveUtil import save_random_file
import my_bot
import time
period = 3600


save_random_file()
try:
    my_bot.upload_media()
    print("uploaded")
except:
    print("didn't uploaded")
my_bot.auto_follow_back()


