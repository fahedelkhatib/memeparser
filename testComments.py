import praw

r = praw.Reddit(client_id='LJ2JgRga7CP6Cw',
             client_secret='WJ-I1ZbsCVz8F3Tz-XFyua7iqhE',
             user_agent='windows:com.mrfalafel.memescraper:v1.0.0'
             )

#these two functions were obtained from the following stackoverflow thread
#https://stackoverflow.com/questions/36366388/get-all-comments-from-a-specific-reddit-thread-in-python/36377995#36377995
#thank you to OP for making my life wildly easier
def getSubComments(comment, allComments, verbose=True):
  allComments.append(comment)
  if not hasattr(comment, "replies"):
    replies = comment.comments()
    if verbose: print("fetching (" + str(len(allComments)) + " comments fetched total)")
  else:
    replies = comment.replies
  for child in replies:
    getSubComments(child, allComments, verbose=verbose)

def getAll(r, submissionId, verbose=True):
  submission = r.submission(submissionId)
  comments = submission.comments
  commentsList = []
  for comment in comments:
    getSubComments(comment, commentsList, verbose=verbose)
  return commentsList

def printComments(r, submissionId, verbose=True):
    commentsList = getAll(r, submissionId)
    for comment in commentsList:
        print(comment.body)

printComments(r, "nv2py6")