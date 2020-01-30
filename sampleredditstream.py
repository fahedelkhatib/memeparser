import praw
import time
import os
import wget
from zipfile import ZipFile #play with this after figuring out how to name files
#from datetime import datetime

def initializeRedditInstance():
    redditObject = praw.Reddit(client_id='LJ2JgRga7CP6Cw',
             client_secret='WJ-I1ZbsCVz8F3Tz-XFyua7iqhE',
             user_agent='windows:com.mrfalafel.memescraper:v1.0.0'
             )
    return redditObject

def getTitleasTimestamp():
    print('\t\tgetting time for use in timestamp')
    #now = datetime.now().time()

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print('\t\t' + current_time)
    current_time = changeWord(current_time)
    return current_time

    #print("\t\tnow =", now)
    #print("\t\ttype(now) =", type(now))
    #return now

def changeWord(word):
    print('\treplacing : with _ in timestamp')
    for letter in word:
        if letter == ":":
            word = word.replace(letter,"_")
    print('\tNEW WORD: ' + word)
    return word

#passes in submission object from reddit.stream.submissions()
#meant to be called in for loop iterating through reddit.stream.submissions()
def printPostInformation(submission):
    print('Post title: ' + str(submission.title.encode('utf-8')))
    print('Post URL: ' + str(submission.url.encode('utf-8')))
    #the .author below instantiates a "redditor" instance... just fyi :)
    #print('Post Author: ' + str(submission.author.name.encode('utf-8')))
    print('Post Author: ' + str(submission.author.name.encode('utf-8')))
    #print(getTitleasTimestamp())

##################################################################################
##################################################################################


reddit = initializeRedditInstance()

os.system('cls')


print('okay, so you got this far')
subredditname = input('so then... tell me which subreddit you want to monitor habibi :)\n')


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
    

    printPostInformation(submission)
    

    try:
        print('1: --trying--')

        filename = wget.download(submission.url)    #saves filename while simultaneously attempting download
        print('\nFILENAME: ' + str(filename))         #prints filename for logging purposes

        
        print('2: --gettingTimestamp--')

        now = getTitleasTimestamp()                 #gets timestamp and saves it to 'now' variable
        
        print('3: --scanningforbadfiletypes--')

        if(str(filename).endswith(".wget")):
            os.remove(filename)
            print("\nFILE REMOVED")
            
        print('4: --humaninputbuffer--')
        
        #humaninputbuffer = input('renaming file')
        
        print('5: renaming file')
        
        os.rename(filename, str(now))
        filename = str(now)
        print('NEW FILENAME: ' + filename)
        
        print('6: completed try')
        
        
    except:
        print('-1')
        print('\nNOTHING DOWNLOADED')
        #imagescounted = imagescounted - 1

    
    print('\n******************************************************')
    if(loops >= 10):
        break;
    #print(str(submission.description.encode('utf-8')))
    #print(str(comment))
    time.sleep(0.75)

print('number of times looped: ' + str(loops))
