import praw
import time
import re

# Log into reddit
def authenticate():
    print('Authenticating...')
    reddit = praw.Reddit('AnimeThemeBot', user_agent = 'Comments with link to anime op/ed as request, v0.1')
    print('Authenticated as {}'.format(reddit.user.me()))
    return reddit

# Get 25 comments and see if anyone requested an OP/ED using "!op" or "!ed"
def run_bot(reddit):
    comment = 'Here are the openings I found: '
    # URLs for opening and endings go in these arrays
    openingArray = []
    endingArray = []
    print('Obtaining 25 comments')
    for comment in reddit.subreddit('test').comments(limit=25):
        for match in re.finditer('!op\((.*)\)', comment.body, re.S):
            # Fills the array with anime opening URLs
            for submission in reddit.subreddit('animethemes').search(match.group(1)):
                openingArray.append(submission.url)
            openingNumber = 0
            for url in openingArray:
                openingNumber += 1
                comment += '[OP #' + openingNumber + '] ' + url # TODO
                print(comment)
    print('Resting for 10 seconds...')
    time.sleep(10)


def main():
    reddit = authenticate()
    while(True):
        run_bot(reddit)

if __name__ == '__main__':
    main()
