import praw
import time
import os


def initializeRedditInstance():
    redditObject = praw.Reddit(client_id='LJ2JgRga7CP6Cw',
             client_secret='WJ-I1ZbsCVz8F3Tz-XFyua7iqhE',
             user_agent='windows:com.mrfalafel.memescraper:v1.0.0'
             )
    return redditObject

reddit = initializeRedditInstance()

os.system('cls')


print('okay so you got this far')
subredditname = input('so then... tell me which subreddit you want to monitor :)\n')

loops = 0
subreddit = reddit.subreddit(subredditname)
print('PRINTING POST STREAM FROM SUBREDDIT: r/' + subreddit.display_name + '\n\n')
#print(subreddit.display_name)

for submission in subreddit.stream.submissions(skip_existing=True):
    loops = loops + 1
    print('******************************************************')
    print(str(submission.title.encode('utf-8')))
    print(str(submission.url.encode('utf-8')))
    print('******************************************************')
    
    #print(str(submission.description.encode('utf-8')))
    #print(str(comment))
    time.sleep(0.5)

print('number of times looped: ' + str(loops))
