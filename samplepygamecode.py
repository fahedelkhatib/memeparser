import pygame
import os
from gtts import gTTS


pygame.mixer.init()
print('success!')

filename='Bruh Sound Effect #2-2ZIpFytCSVc.wav'
#tts = gTTS(text='this should be an error message!', lang='en-au')
#tts.save(filename)
sound1 = pygame.mixer.Sound(filename)
