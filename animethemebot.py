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
    print('Obtaining 25 comments')
    for comment in reddit.subreddit('test').comments(limit=25):
        for match in re.finditer('!op\((.*)\)', comment.body, re.S):
            print('This was what was commented: {}'.format(match.group(1)))
    print('Resting for 10 seconds...')
    time.sleep(10)


def main():
    reddit = authenticate()
    while(True):
        run_bot(reddit)

if __name__ == '__main__':
    main()
