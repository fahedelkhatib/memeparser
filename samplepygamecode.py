import pygame
import os
from gtts import gTTS


pygame.mixer.init()


filename='Bruh Sound Effect #2-2ZIpFytCSVc.mp3'
#tts = gTTS(text='bruh', lang='en-au')
#tts.save(filename)
os.system('mpg321 filename')
os.system('dir')
pygame.mixer.music.load(filename)
pygame.mixer.music.play(2)
#sound1.play(0)

print('success!')
