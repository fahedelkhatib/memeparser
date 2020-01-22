#import selenium
import praw
#from gtts import gTTS
import time
import os
import pygame
import wget
#import re

#uses pygame.mixer.music the wrong way but plays tts files one at a time
def play(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    #if pygame.mixer.music.get_busy() == True :
    pygame.mixer.music.queue(filename)    
    pygame.mixer.music.play()
    #return pygame.mixer.Sound.get_length()
    print('ADDED MP3 TO QUEUE')

#opens file and commits contents to python string
def stringifyfile(inputfilename):
    inputfile = open(inputfilename)
    input1 = ' '
    for line in inputfile:
        input1 += line
    print("TEXT BEING READ TO STRING: \n" + input1)
    return input1

#playsdebugmessage of choice
def playdebugmessage(debugmessagetitle):
    filename = debugmessagetitle
    input1 = 'take 2 subreddit pull complete'
    #tts = gTTS(text=input1,lang='es')
    #tts.save(filename)
    play(filename)
    print('debugmessage played\n')

#initializes, returns reddit instance using PRAW
def initializeRedditInstance():
    redditObject = praw.Reddit(client_id='LJ2JgRga7CP6Cw',
             client_secret='WJ-I1ZbsCVz8F3Tz-XFyua7iqhE',
             user_agent='windows:com.mrfalafel.memescraper:v1.0.0'
             )
    return redditObject

#my favorite feature owo)/
def subredditpullcompleted():
    srpc = "subredditpullcompleted.mp3"
    #playdebugmessage("subredditpullcompleted.mp3")
    playdebugmessage(srpc.encode('utf-8'))
    #playdebugmessage(srpc)
    time.sleep(4)

#this one straight up is just here so i can reference a piece of useful code
def getimg(self):
    self.all = self.reddit.subreddit('all').new(limit=10)

    for post in self.all:
        if str(post.url).endswith('.jpg'):
            try:
                response = urllib.request.urlopen(post.url)
            except:
                break
            self.img = response.read()
            with open(str(post.id)+'.jpg','wb') as f:
                f.write(self.img)

def displayAnalytics(imagesqueried, imagescounted):
    print('\n\n\t\t---------DISPLAYING ANALYTICS---------\n\n')
    print('PREVIOUS DIRECTORY: ')
    print(os.getcwd())
    #'C:\\Users\\pc\\Documents\\memeparser'
    os.chdir(homedirectory)
    print('WORKING DIRECTORY: ')
    print(os.getcwd())
    print('IMAGES QUERIED: ' + str(imagesqueried))
    print('IMAGES DOWNLOADED: ' + str(imagescounted))
    print('\n\n\t\t-----------END OF ANALYTICS-----------\n\n')

####################################################################
####################################################################


os.system('cls')
#os.system('mpg123 subredditpullcompleted.mp3')
#os.system('ren bruh.wav bruhh.wav')
os.system('echo hello, people of earth!')
#os.system('python -m wget https://www.reddit.com/r/MicrowavedMemes/ -o FILE ')
homedirectory = str(os.getcwd())


reddit = initializeRedditInstance()

subreddit = reddit.subreddit('redditdev')

print(reddit.domain('imgur.com').new())

print(subreddit.display_name)
print(subreddit.title)
#print(subreddit.description)

for submission in subreddit.new(limit=7):
    print(submission.title)    
    #print(reddit.read_only)
    time.sleep(0.1)
    print('---------------------------------------------')

subredditpullcompleted()

#######################################################################
#######################################################################


#regex = re.compile('.jpg')
querylimit= int(input('how many entries should i query?\n'))
subredditname = input("Enter subreddit name: ")
bVerifySubreddit = input("Are you sure? (answer True or False)\n")

while((bVerifySubreddit != "True") & (bVerifySubreddit != "true") & (bVerifySubreddit != "T") & (bVerifySubreddit != "t")):
    subredditname = input("Enter subreddit name again: ")
    bVerifySubreddit = input("Are you sure? (answer True or False)\n")

downloadpath = input("Where would you like to download these memes? \n")#.encode('utf-8')
print("the path you have chosen is: " + str(downloadpath))


submissions = reddit.subreddit(subredditname).top(limit=querylimit)
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

for submission in submissions:
    print(submission.title.encode('utf-8'), submission.url.encode('utf-8'))
    try:
        wget.download(submission.url)
        imagescounted = imagescounted + 1
        imagesqueried = imagesqueried + 1
    except:
        print('NOTHING DOWNLOADED')
        imagescounted = imagescounted - 1
    time.sleep(1)
    print('\nquery concluded')
    print('\n---------------------------------------------')


displayAnalytics(imagesqueried, imagescounted)
subredditpullcompleted()
