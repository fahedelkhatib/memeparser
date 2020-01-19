import selenium
import praw
from gtts import gTTS
import time
import os
import pygame

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

def playdebugmessage(debugmessagetitle):
    filename = debugmessagetitle
    input1 = 'bruh'
    #tts = gTTS(text=input1,lang='es')
    #tts.save(filename)
    play(filename)
    print('debugmessage played\n')

def initializeRedditInstance():
    redditObject = praw.Reddit(client_id='LJ2JgRga7CP6Cw',
             client_secret='WJ-I1ZbsCVz8F3Tz-XFyua7iqhE',
             user_agent='windows:com.mrfalafel.memescraper:v1.0.0'
             )
    return redditObject

####################################################################
####################################################################


os.system('cls')
#os.system('ren bruh.wav bruhh.wav')
os.system('echo hello world!')
#os.system('python -m wget https://www.reddit.com/r/MicrowavedMemes/ -o FILE ')

reddit = initializeRedditInstance()

subreddit = reddit.subreddit('nukedmemes')

print(reddit.domain('imgur.com').new())

#print(subreddit.display_name)
#print(subreddit.title)
#print(subreddit.description)

for submission in reddit.subreddit('nukedmemes').new(limit=20):
    print(submission.title)
    #print(reddit.read_only)
    time.sleep(0.5)
    print('---------------------------------------------')


playdebugmessage('subredditpullcompleted.mp3')
time.sleep(4)


