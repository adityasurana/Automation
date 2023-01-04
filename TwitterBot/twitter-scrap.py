from concurrent.futures import ThreadPoolExecutor
from tweepy import OAuthHandler
from tweepy import API
import tweepy
import pandas as pd
import sys, os, time, shutil
# from zipfile import ZipFile
from datetime import datetime

#Twitter API credentials
consumer_key = "***"
consumer_secret = "***"
access_token = "***"
access_token_secret = "***"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

screen_name = "FAmagazine"
  
# getting only 30 followers
for follower in api.followers(screen_name):
    print(follower.screen_name)


def make_archive(source, destination):
    base = os.path.basename(destination)
    name = base.split('.')[0]
    format = base.split('.')[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    print(source, destination, archive_from, archive_to)
    shutil.make_archive(name, format, archive_from, archive_to)
    shutil.move('%s.%s'%(name,format), destination)
    return 0

def get_all_tweets(screen_name):
    flag = 0
    tweet_id =        []
    tweet_time =      []
    tweet_text =      []
    usr_screen_name = []
    
    alltweets = []
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    
    while len(new_tweets) > 0:

        #print("getting tweets before tweet id %s" % (oldest))
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))
        for tweet in alltweets:
            if tweet.created_at < endDate and tweet.created_at > startDate:
                tweet_id.append(str(tweet.id_str))
                tweet_time.append(tweet.created_at)
                tweet_text.append(tweet.text)
                usr_screen_name.append(screen_name)

    print("len of tweet_id:", len(tweet_id))

    df = pd.DataFrame()
    df['User Screen Name'] = usr_screen_name
    df['Tweet Id'] = tweet_id
    df['Tweet Time'] = tweet_time
    df['Tweet Text'] = tweet_text
    
    df.to_excel("twitter_output.xlsx", index=False)
    
    make_archive('uploads/media/%s/output_folder' %(arg_taken), 'uploads/media/%s/zipfolder/tweet.zip' %(arg_taken))
     
    while flag == 0:
        df['Retweet_Count'] = ''
        df['Like_Count'] = ''
        flag = 1

    count = 0
    indexer = 0
    while count < len(tweet_id):
        retweet_count =   []
        like_count =      []
        temp = 1
        while temp<=10 and count<len(tweet_id):
            try:
                tweets = api.get_status(int(tweet_id[count]))
                try:
                    retweet_count.append(tweets.retweet_count)
                    like_count.append(tweets.favorite_count)
                    temp = temp + 1
                    count = count + 1
                except:
                    retweet_count.append(0)
                    like_count.append(0)
                    temp = temp + 1
                    count = count + 1
            except:
                retweet_count.append('')
                like_count.append('')
                temp = temp + 1
                count = count + 1
                time.sleep(60)
                  
        df.Retweet_Count.iloc[indexer:indexer+len(retweet_count)] = retweet_count
        df.Like_Count.iloc[indexer:indexer+len(like_count)] = like_count
        indexer = indexer + 10
        df.to_excel("twitter_output.xlsx", index=False)
        
        make_archive('uploads/media/%s/output_folder' %(arg_taken), 'uploads/media/%s/zipfolder/tweet.zip' %(arg_taken))

def arg_str(arg_taken):
    return arg_taken

arg_taken = arg_str(sys.argv[1])
print(arg_taken)

fromDate = sys.argv[2]
toDate =   sys.argv[3]

from_year = fromDate.split("-")[0]
from_month = fromDate.split("-")[1]
from_day = fromDate.split("-")[1:][-1]
fromDate = "%s-%s-%s" %(from_day, from_month, from_year)

to_year = toDate.split("-")[0]
to_month = toDate.split("-")[1]
to_day = toDate.split("-")[1:][-1]
toDate = "%s-%s-%s" %(to_day, to_month, to_year)

startDate = datetime.strptime(fromDate, '%d-%m-%Y')
endDate = datetime.strptime(toDate, '%d-%m-%Y')


dir_path = os.path.dirname(os.path.realpath(__file__))
inputpath = "%s/%s/input_folder" % (dir_path,arg_taken)
filename=""
for f in os.listdir(inputpath):
    filename = f

twitter_df = pd.read_excel("inputTwitterUsername.xlsx")
executor = ThreadPoolExecutor(max_workers=10)
for i in twitter_kol.iloc[0:,0].unique():
    j=i
    a = executor.submit(get_all_tweets, j)
    
