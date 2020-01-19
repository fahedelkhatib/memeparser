import selenium
import praw
from gtts import gTTS
import time
import os
import pygame
import wget
import re

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
    input1 = 'bruh'
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

def subredditpullcompleted():
    srpc = "C:\\Users\\pc\\Dropbox\\UltimaCode\\Python\\memeparser\\subredditpullcompleted.mp3"
    playdebugmessage(srpc.encode('utf-8'))
    time.sleep(2)

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

####################################################################
####################################################################


os.system('cls')
#os.system('ren bruh.wav bruhh.wav')
os.system('echo hello, people of earth!')
#os.system('python -m wget https://www.reddit.com/r/MicrowavedMemes/ -o FILE ')

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

#subredditpullcompleted()

#regex = re.compile('.jpg')
subredditname = input("Enter subreddit name: ")

submissions = reddit.subreddit(subredditname).top(limit=3000)
try:
    os.mkdir(subredditname)
except:
    print(subredditname + " DIRECTORY ALREADY EXISTS")

print('WORKING DIRECTORY: ')
#os.system('cd nukedmemes')
os.chdir(subredditname)
os.system('pwd')
for submission in submissions:
    print(submission.title.encode('utf-8'), submission.url.encode('utf-8'))
    try:
        wget.download(submission.url)
    except:
        
        print('NOTHING DOWNLOADED')
    time.sleep(1)
    print('---------------------------------------------')
    
os.chdir('../')
os.system('pwd')
subredditpullcompleted()
