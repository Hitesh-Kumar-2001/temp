from DriveUtil import save_random_file
import my_bot
import time
period = 3600


while(True):
    save_random_file()
    my_bot.upload_media()
    my_bot.auto_follow_back()
    time.sleep(period)