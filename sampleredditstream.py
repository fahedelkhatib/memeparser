import praw
import time
from time import gmtime, strftime
import os
import wget
#from zipfile import ZipFile #play with this after figuring out how to name files
#from datetime import datetime
import pygame
#import ffmpeg

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
    current_time = strftime("%a,%d%b%Y_%H_%M_%S", t)
    #strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    #time.strftime("%H:%M:%S", t)
    print('\t\t' + current_time)

    

    print('\t\tCURRENT_TIME: ' + current_time)
    #current_time = 't_' + changeWord(current_time)
    #print("\t\tnow =", now)
    #print("\t\ttype(now) =", type(now))
    #return now
    
    return current_time
def changeWord(word):
    print('\treplacing : with _ in timestamp')
    for letter in word:
        if letter == ":":
            word = word.replace(letter,"_")
    print('\tNEW WORD: ' + word)
    return word
def returnOldFileExtension(filename):

    if(str(filename).endswith('.jpg')):
       return '.jpg'
    if(str(filename).endswith('.png')):
       return '.png'
    if(str(filename).endswith('.gif')):
       return '.gif'
    if(str(filename).endswith('.pdf')):
       return '.pdf'
    if(str(filename).endswith('.mp3')):
       return '.mp3'
    if(str(filename).endswith('.mp4')):
        return '.mp4'
    if(str(filename).endswith('.wav')):
        return '.wav'

    print('\nfile is not among accepted filetypes')
    return 'file'
def vetFileExtension(filename):
    
    if(str(filename).endswith(".wget") |
       str(filename).endswith(".download") |
       str(filename).endswith(".html") |
       str(filename).endswith(".tmp") |
       (returnOldFileExtension(filename) == 'file') |
       str(filename).endswith(".php") |
       str(filename).endswith(".WGET")):
            os.remove(filename)
            print("\nFILE REMOVED")
def displayAnalytics(imagesqueried, imagescounted):
    print('\n\n\t\t---------DISPLAYING ANALYTICS---------\n\n')
    print('PROCESS ID: ' + str(os.getpid()))
    print('PREVIOUS DIRECTORY: ')
    print(downloadpath)
    #print(os.getcwd())
    #'C:\\Users\\pc\\Documents\\memeparser'
    os.chdir(homedirectory)
    print('WORKING DIRECTORY: ')
    print(os.getcwd())
    print('IMAGES QUERIED: ' + str(imagesqueried))
    print('IMAGES DOWNLOADED: ' + str(imagescounted))
    print('\n\n\t\t-----------END OF ANALYTICS-----------\n\n')
#passes in submission object from reddit.stream.submissions()
#meant to be called in for loop iterating through reddit.stream.submissions()
def printPostInformation(submission, debugLogFileName):
    
    outputString = ''
    outputLogFile = open(debugLogFileName, 'w')
    
    print('Post title: ' + str(submission.title.encode('utf-8')))
    outputString = outputString + '\nPost title: ' + str(submission.title.encode('utf-8'))
    #print('Post title: ' + str(submission.title.encode('utf-8')), file = outputLogFile)
    
    print('Post URL: ' + str(submission.url.encode('utf-8')))
    outputString = outputString + '\nPost URL: ' + str(submission.url.encode('utf-8'))

    #the .author below instantiates a "redditor" instance... just fyi :)
    print('Post Author: ' + str(submission.author.name.encode('utf-8')))
    outputString = outputString + '\nPost Author: ' + str(submission.author.name.encode('utf-8'))
    
    print('Number of Comments: ' + str(submission.num_comments))
    outputString = outputString + '\nPost Author: ' + str(submission.num_comments)

    print('Subreddit Name: ' + str(submission.subreddit.display_name.encode('utf-8')))
    outputString = outputString + '\nPost Author: ' + str(submission.author.name.encode('utf-8'))

        
    print(outputString, file = outputLogFile)
#my favorite feature owo)/
def subredditpullcompleted():
    srpc = "subredditpullcompleted.mp3"
    #playdebugmessage("subredditpullcompleted.mp3")
    playdebugmessage(srpc)
    #playdebugmessage(srpc.encode('utf-8'))
    #playdebugmessage(srpc)
    time.sleep(4)
def playdebugmessage(debugmessagetitle):
    filename = debugmessagetitle
    input1 = 'take 2 subreddit pull complete'
    #tts = gTTS(text=input1,lang='es')
    #tts.save(filename)
    play(filename)
    print('debugmessage played\n')
def play(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    #if pygame.mixer.music.get_busy() == True :
    pygame.mixer.music.queue(filename)    
    pygame.mixer.music.play()
    #return pygame.mixer.Sound.get_length()
    print('ADDED MP3 TO QUEUE')

##################################################################################
##################################################################################

showDebugMessages = False 
imagescounted = 0
imagesqueried = 0
reddit = initializeRedditInstance()
homedirectory = os.getcwd()
debugLogFileName = 'C:\\users\\felicity\\documents\\memeparser\\debuglog.txt'


os.system('cls')
print('okay, so you got this far')
subredditname = input('so then... tell me which subreddit you want to monitor habibi :)\n')
subredditname = 'all'

#querylimit= int(input('how many entries should i query?\n'))
#subredditname = input("Enter subreddit name: ")
bVerifySubreddit = input("Are you sure? I don't judge! (answer True or False)\n")
bVerifySubreddit = 't'
#while loop to verify subreddit name inputted
while((bVerifySubreddit != "True") &
      (bVerifySubreddit != "true") &
      (bVerifySubreddit != "T") &
      (bVerifySubreddit != "t") &
      (bVerifySubreddit != "y") &
      (bVerifySubreddit != "Yes") &
      (bVerifySubreddit != "yes")):
    subredditname = input("Enter subreddit name again: ")
    bVerifySubreddit = input("Are you sure? (answer True or False)\n")

downloadpath = input("Where would you like to download these memes? \n")#.encode('utf-8')
downloadpath = 'C:\\users\\felicity\\documents\\niggabuffer'
print("The path you have chosen is: " + str(downloadpath))


#submissions = reddit.subreddit(subredditname).top(limit=querylimit)
try: #attempts to create directory path chosen
    os.mkdir(downloadpath)
    print('NEW DIRECTORY CREATED')
except: #throws error message if directory already exists
    print("-------" + downloadpath + " DIRECTORY ALREADY EXISTS-------")

print('WORKING DIRECTORY: ')
#os.system('cd nukedmemes')
os.chdir(downloadpath)
print(os.getcwd())






##################################################################################
##################################################################################





loops = 0
subreddit = reddit.subreddit(subredditname)
print('PRINTING POST STREAM FROM SUBREDDIT: r/' + subreddit.display_name + '\n\n')
#print(subreddit.display_name)

for submission in subreddit.stream.submissions(skip_existing=True):

    loops = loops + 1
    printPostInformation(submission, debugLogFileName)
    
    try:
        if(showDebugMessages):
            print('1: --trying--')

        filename = wget.download(submission.url)
        if(filename != 'download.wget'):
            imagesqueried = imagesqueried + 1
        else:
            print('\t\t\tUH OH! YOU FUCKING BUFFOON! YOU MORON!')
        #saves filename while simultaneously attempting download
        print('\nFILENAME: ' + str(filename))
        #prints filename for logging purposes

        if(showDebugMessages):
            print('2: --gettingTimestamp--')

        now = getTitleasTimestamp()
        #gets timestamp and saves it to 'now' variable
        
        if(showDebugMessages):
            print('3: --scanningforbadfiletypes--')

        vetFileExtension(filename)

        if(showDebugMessages):
            print('function call: retaining old file extension')
        oldFileExtension = returnOldFileExtension(filename)
        
        if(showDebugMessages):
            print('4: --humaninputbuffer--')
        
        #humaninputbuffer = input('renaming file')
        
        if(showDebugMessages):
            print('5: renaming file')
        now = now + oldFileExtension
        os.rename(filename, str(now))
        filename = str(now)
        print('NEW FILENAME: ' + filename)
        
        if(showDebugMessages):
            print('6: completed try')
        imagescounted = imagescounted + 1
            
    except:
        if(showDebugMessages):
            print('-1')
        print('\n--------FAIL MESSAGE---------')
        #imagescounted = imagescounted - 1

    print('\n******************************************************')
    if(loops >= 100):
        break;
    #print(str(submission.description.encode('utf-8')))
    #print(str(comment))
    time.sleep(0.75)

print('number of times looped: ' + str(loops))
os.chdir(homedirectory)
displayAnalytics(imagesqueried, imagescounted)
subredditpullcompleted()
