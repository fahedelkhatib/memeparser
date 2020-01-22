import praw
import time

def initializeRedditInstance():
    redditObject = praw.Reddit(client_id='LJ2JgRga7CP6Cw',
             client_secret='WJ-I1ZbsCVz8F3Tz-XFyua7iqhE',
             user_agent='windows:com.mrfalafel.memescraper:v1.0.0'
             )
    return redditObject

reddit = initializeRedditInstance()


print('okay so you got this far')


loops = 0
subreddit = reddit.subreddit('all')
print('PRINTING POST STREAM FROM SUBREDDIT: r/' + subreddit.display_name + '\n\n')
#print(subreddit.display_name)

for submission in subreddit.stream.submissions(skip_existing=True):
    loops = loops + 1
    print(str(submission.title.encode('utf-8')))
    #print(str(submission.description.encode('utf-8')))
    #print(str(comment))
    time.sleep(0.5)

print('number of times looped: ' + str(loops))
