import selenium
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

def playdebugmessage():
    filename = 'debugmessage.mp3'
    input1 = 'bruh'
    tts = gTTS(text=input1,lang='es')
    tts.save(filename)
    os.system('mpg321 filename')
    play(filename)
    #pygame.mixer.init()
    #pygame.mixer.music.load(filename)
    #pygame.mixer.music.play(0)
    print('debugmessage played\n')

os.system('cls')
os.system('ren bruh.wav bruhh.wav')
os.system('echo \n')
os.system('echo hello world!')
#os.system('python -m wget https://www.reddit.com/r/MicrowavedMemes/ -o FILE ')
playdebugmessage()




