bpygame = True;

import praw
import time
#from time import gmtime, strftime
import os
import wget
#from zipfile import ZipFile #play with this after figuring out how to name files
from datetime import datetime

if(bpygame == True):
    import pygame
#import ffmpeg

def initializeRedditInstance():
    redditObject = praw.Reddit(client_id='LJ2JgRga7CP6Cw',
             client_secret='WJ-I1ZbsCVz8F3Tz-XFyua7iqhE',
             user_agent='windows:com.mrfalafel.memescraper:v1.0.0'
             )
    return redditObject

def getTitleasTimestamp(submission, showDebugMessages):
    if(showDebugMessages == True):
        print('\t\tgetting timestamp from API')
    t = submission.created_utc
    if(showDebugMessages == True):
        print("\t\tt = " + str(t))
    timestamp = datetime.utcfromtimestamp(t).strftime('%a,%d%b%Y_%H_%M_%S')
    if(showDebugMessages == True):
        print('\t\tTIMESTAMP: ' + timestamp)
    return timestamp

def changeWord(word, showDebugMessages):
    if(showDebugMessages == True):
        print('\treplacing : with - in word')
    for letter in word:
        if letter == ":":
            word = word.replace(letter,"-")
    if(showDebugMessages == True):
        print('\tNEW WORD: ' + word)
    
    if(showDebugMessages == True):
        print('\treplacing various characters with _ in word: ' + word)
    for letter in word:
        #this could have been one giant if statement, but i added them all separately for readability
        #bazinga
        if letter == " ":
            word = word.replace(letter,"_")
        if letter == "\\":
            word = word.replace(letter,"_")
        if letter == "/":
            word = word.replace(letter,"_")
        if letter == "*":
            word = word.replace(letter,"_")
        if letter == "?":
            word = word.replace(letter,"_")
        if letter == "<":
            word = word.replace(letter,"_")
        if letter == ">":
            word = word.replace(letter,"_")
        if letter == "|":
            word = word.replace(letter,"_")
        if letter == ".":
            word = word.replace(letter,"_")
    if(showDebugMessages == True):
        print('\tNEW WORD: ' + word)
    return str(word)
    
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
    print('Post title: ' + str(submission.title.encode('utf-8')))
    print('Post URL: ' + str(submission.url.encode('utf-8')))
    print('Post Author: ' + str(submission.author.name.encode('utf-8')))
    print('Number of Comments: ' + str(submission.num_comments))
    print('Subreddit Name: ' + str(submission.subreddit.display_name.encode('utf-8')))

def savePostInformation(submission, debugLogFileName):
    outputString = ''
    outputLogFile = open(debugLogFileName, 'w')
    outputString = outputString + '\nPost title: ' + str(submission.title.encode('utf-8'))
    outputString = outputString + '\nPost URL: ' + str(submission.url.encode('utf-8'))
    outputString = outputString + '\nPost Author: ' + str(submission.author.name.encode('utf-8'))
    outputString = outputString + '\nNumber of Comments: ' + str(submission.num_comments)
    outputString = outputString + '\nSubreddit Name: ' + str(submission.subreddit.display_name.encode('utf-8'))
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

def createNewDirectoryAndChDir(downloadpath):
    try: #attempts to create directory path chosen
        os.mkdir(downloadpath)
        print('NEW DIRECTORY CREATED')
    except: #throws error message if directory already exists
        print("-------" + downloadpath + " DIRECTORY ALREADY EXISTS-------")
        
    print('WORKING DIRECTORY: ')
    #os.system('cd nukedmemes')
    os.chdir(downloadpath)
    print(os.getcwd())
    
def createSubredditInstance(reddit, subredditname):
    subreddit = reddit.subreddit(subredditname)
    print('PRINTING POST STREAM FROM SUBREDDIT: r/' + subreddit.display_name + '\n\n')
    #print(subreddit.display_name)

    subredditstream = reddit.subreddit(subredditname).stream.submissions(skip_existing=False)
    
    return subredditstream

def printFailMessage(now, loops, showDebugMessages):
    if(showDebugMessages):
        print("\n\t\tGENERATING FAILURE REPORT")
        if(now):
            print("\t\t\tFinal Title: " + str(now))
        else:
            print("\t\t\ttitle not created yet")
        print("\t\t\tLoop Number: " + str(loops))
    

def mainRedditLoop(subredditstream, showDebugMessages, debugLogFileName):

    imagescounted = 0
    imagesqueried = 0
    loops = 0

    for submission in subredditstream:
    #for submission in subreddit.stream.submissions(skip_existing=False):
        print("Loop Number: " + str(loops))
        print("Loop Time: " + str(time.strftime("%c,%H")))
        print("Number downloaded: " + str(imagescounted))
        loops = loops + 1
        printPostInformation(submission, debugLogFileName)
        
        try:
            if(showDebugMessages):
                print('1: --trying--')

            filename = wget.download(submission.url)
            print('\n\t\tdownload failed successfuly')
            
            #saves filename while simultaneously attempting download
            print('\nFILENAME: ' + str(filename))
            #prints filename for logging purposes

            if(showDebugMessages):
                print('2: --gettingTimestamp--')

            now = getTitleasTimestamp(submission, showDebugMessages)
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
            subredditname = submission.subreddit.display_name
            
            if(showDebugMessages):
                print('5.1: renaming file')
            title = submission.title
            
            if(showDebugMessages):
                print('5.2: renaming file')
            now = now + "__" + title + "__" + subredditname + "__"
            
            if(showDebugMessages):
                print('5.3: renaming file')
            now = str(changeWord(str(now), showDebugMessages)) + str(oldFileExtension)
            
            if(showDebugMessages):
                print('5.4: renaming file')
                print("5.4: working directory: " + str(os.getcwd()))
            #time.sleep(5)
            os.rename(filename, now)
            
            if(showDebugMessages):
                print('5.5: renaming file')
            filename = str(now)
            
            if(showDebugMessages):
                print('5.6: renaming file')
            print('NEW FILENAME: ' + filename)
            
            if(showDebugMessages):
                print('6: completed try')
            imagescounted = imagescounted + 1
                
        except:
        
            if(showDebugMessages):
                print('-1')
            print('\n--------FAIL MESSAGE---------')
            printFailMessage(now, loops, showDebugMessages)
            #imagescounted = imagescounted - 1

        print('\n******************************************************')
        if(loops >= 10000):
            break;
        #print(str(submission.description.encode('utf-8')))
        #print(str(comment))
        time.sleep(1)



##################################################################################
##################################################################################

#showDebugMessages = False
#imagescounted = 0
#imagesqueried = 0
#reddit = initializeRedditInstance()
#homedirectory = os.getcwd()
#debugLogFileName = 'C:\\users\\pc\\documents\\memeparser\\debuglog.txt'


#os.system('cls')
#print('okay, so you got this far')
#subredditname = input('so then... tell me which subreddit you want to monitor habibi :)\n')
#subredditname = 'nukedmemes'



#bVerifySubreddit = input("Are you sure? I don't judge! (answer True or False)\n")

#while loop to verify subreddit name inputted
#while((bVerifySubreddit != "True") &
#      (bVerifySubreddit != "true") &
#      (bVerifySubreddit != "T") &
#      (bVerifySubreddit != "t") &
#      (bVerifySubreddit != "y") &
#      (bVerifySubreddit != "Yes") &
#      (bVerifySubreddit != "yes")):
#    subredditname = input("Enter subreddit name again: ")
#    bVerifySubreddit = input("Are you sure? (answer True or False)\n")

#downloadpath = input("Where would you like to download these memes? \n")#.encode('utf-8')
#downloadpath = 'C:\\users\\pc\\documents\\buffer'
#print("The path you have chosen is: " + str(downloadpath))



#submissions = reddit.subreddit(subredditname).top(limit=querylimit)

#try: #attempts to create directory path chosen
#    os.mkdir(downloadpath)
#    print('NEW DIRECTORY CREATED')
#except: #throws error message if directory already exists
#    print("-------" + downloadpath + " DIRECTORY ALREADY EXISTS-------")

#print('WORKING DIRECTORY: ')
#os.system('cd nukedmemes')
#os.chdir(downloadpath)
#print(os.getcwd())

##################################################################################
##################################################################################

#loops = 0
#subreddit = reddit.subreddit(subredditname)
#print('PRINTING POST STREAM FROM SUBREDDIT: r/' + subreddit.display_name + '\n\n')
#print(subreddit.display_name)

#subredditstream = reddit.subreddit("nukedmemes+deepfriedmemes+bingbongtheorem").stream.submissions(skip_existing=False)

#for submission in subredditstream:
##for submission in subreddit.stream.submissions(skip_existing=False):
#    print("Loop Number: " + str(loops))
#    print("Loop Time: " + str(time.strftime("%c,%H")))
#    print("Number downloaded: " + str(imagescounted))
#    loops = loops + 1
#    printPostInformation(submission, debugLogFileName)
    
#    try:
#        if(showDebugMessages):
#            print('1: --trying--')

#        filename = wget.download(submission.url)
#        print('\n\t\tdownload failed successfuly')
        
#       #saves filename while simultaneously attempting download
#        print('\nFILENAME: ' + str(filename))
#        #prints filename for logging purposes

#        if(showDebugMessages):
#            print('2: --gettingTimestamp--')

#        now = getTitleasTimestamp(submission, showDebugMessages)
        #gets timestamp and saves it to 'now' variable
        
#        if(showDebugMessages):
#            print('3: --scanningforbadfiletypes--')

#        vetFileExtension(filename)

#        if(showDebugMessages):
#            print('function call: retaining old file extension')
#        oldFileExtension = returnOldFileExtension(filename)
        
#        if(showDebugMessages):
#            print('4: --humaninputbuffer--')
        
#        #humaninputbuffer = input('renaming file')
        
#        if(showDebugMessages):
#            print('5: renaming file')
#        subredditname = submission.subreddit.display_name
#        if(showDebugMessages):
#            print('5.1: renaming file')
#        title = submission.title
#        if(showDebugMessages):
#            print('5.2: renaming file')
#        now = now + "__" + title + "__" + subredditname + "__"
#        if(showDebugMessages):
#            print('5.3: renaming file')
#        now = str(changeWord(str(now), showDebugMessages)) + str(oldFileExtension)
#        if(showDebugMessages):
#            print('5.4: renaming file')
#        os.rename(filename, now)
#        if(showDebugMessages):
#            print('5.5: renaming file')
#        filename = str(now)
#        if(showDebugMessages):
#            print('5.6: renaming file')
#        print('NEW FILENAME: ' + filename)
        
#        if(showDebugMessages):
#            print('6: completed try')
#        imagescounted = imagescounted + 1
            
#    except:
#        if(showDebugMessages):
#            print('-1')
#        print('\n--------FAIL MESSAGE---------')
#        #imagescounted = imagescounted - 1

#    print('\n******************************************************')
#    if(loops >= 10000):
#        break;
    #print(str(submission.description.encode('utf-8')))
    #print(str(comment))
#    time.sleep(3)

#print('number of times looped: ' + str(loops))
#os.chdir(homedirectory)
#displayAnalytics(imagesqueried, imagescounted)
#subredditpullcompleted()
