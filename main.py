import selenium
from gtts import gTTS
import time
import os
import pygame

#uses pygame the wrong way but plays tts files one at a time
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
    print("TEXT BEING READ: " + input1)
    return input1


filename = 'debugmessage.wav'
input1 = stringifyfile('harrypotter1911.txt')
tts = gTTS(text=input1 , lang='en-au')
tts.save(filename)
os.system('mpg321 filename')

pygame.mixer.init()
initdebugmessage = pygame.mixer.get_init()
print(initdebugmessage)
scrapealert = pygame.mixer.Sound(file=filename)
pygame.mixer.Sound.play(scrapealert)
print('ayy lmao hello earth')


