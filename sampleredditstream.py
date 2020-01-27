import praw
import time
import os
import wget


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



##################################################################################
##################################################################################



#querylimit= int(input('how many entries should i query?\n'))
#subredditname = input("Enter subreddit name: ")
bVerifySubreddit = input("Are you sure? I don't judge! (answer True or False)\n")

while((bVerifySubreddit != "True") & (bVerifySubreddit != "true") & (bVerifySubreddit != "T") & (bVerifySubreddit != "t")):
    subredditname = input("Enter subreddit name again: ")
    bVerifySubreddit = input("Are you sure? (answer True or False)\n")

downloadpath = input("Where would you like to download these memes? \n")#.encode('utf-8')
print("The path you have chosen is: " + str(downloadpath))


#submissions = reddit.subreddit(subredditname).top(limit=querylimit)
try:
    os.mkdir(downloadpath)
except:
    print("-------" + downloadpath + " DIRECTORY ALREADY EXISTS-------")

print('WORKING DIRECTORY: ')
#os.system('cd nukedmemes')
os.chdir(downloadpath)
print(os.getcwd())

imagescounted = 0
imagesqueried = 0




##################################################################################
##################################################################################





loops = 0
subreddit = reddit.subreddit(subredditname)
print('PRINTING POST STREAM FROM SUBREDDIT: r/' + subreddit.display_name + '\n\n')
#print(subreddit.display_name)

for submission in subreddit.stream.submissions(skip_existing=True):
    loops = loops + 1
    #print('******************************************************')
    print('Post title: ' + str(submission.title.encode('utf-8')))
    print('Post URL: ' + str(submission.url.encode('utf-8')))
    #the .author below instantiates a "redditor" instance... just fyi :)
    #print('Post Author: ' + str(submission.author.name.encode('utf-8')))
    print('Post Author: ' + str(submission.author.name.encode('utf-8')))
    

    try:
        wget.download(submission.url)
        imagescounted = imagescounted + 1
        imagesqueried = imagesqueried + 1
    except:
        print('NOTHING DOWNLOADED')
        imagescounted = imagescounted - 1


    print('\n******************************************************')
    #print(str(submission.description.encode('utf-8')))
    #print(str(comment))
    time.sleep(0.5)

print('number of times looped: ' + str(loops))
