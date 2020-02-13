import functions

showDebugMessages = True

reddit = functions.initializeRedditInstance()
homedirectory = functions.os.getcwd()
debugLogFileName = 'C:\\users\\pc\\documents\\memeparser\\debuglog.txt'

functions.os.system('cls')
print('okay, so you got this far')
subredditname = input('so then... tell me which subreddit you want to monitor, my precious :)\n')
subredditname = 'nukedmemes+deepfriedmemes+gifs+comedyhomicide+trashy+Bossfight+starterpacks+OldSchoolCool+lifehacks+pyrocynical+BuyItForLife+HistoryPorn+FilthyFrank'
#subredditname = 'all'
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
downloadpath = 'C:\\users\\pc\\documents\\buffer'
print("The path you have chosen is: " + str(downloadpath))

functions.createNewDirectoryAndChDir(downloadpath)

subredditstream = functions.createSubredditInstance(reddit, subredditname)

functions.mainRedditLoop(subredditstream, showDebugMessages, debugLogFileName)

print('number of times looped: ' + str(loops))
functions.os.chdir(homedirectory)
functions.displayAnalytics(imagesqueried, imagescounted)
functions.subredditpullcompleted()