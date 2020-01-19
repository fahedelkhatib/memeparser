from gtts import gTTS
import os


tts = gTTS(text='subreddit pull completed', lang='en-au')
tts.save('subredditpullcompleted.wav')
