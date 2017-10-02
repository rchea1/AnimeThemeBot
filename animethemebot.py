import praw
import time
import re
import sqlite3
import os
from datetime import datetime, date

SCRIPT_DIR = os.path.dirname(__file__)
COMMENTS_DB_CONN = sqlite3.connect(os.path.join(SCRIPT_DIR, 'animetheme.db'), detect_types=sqlite3.PARSE_DECLTYPES)
COMMENTS_DB_CURSOR = COMMENTS_DB_CONN.cursor()

# Log into reddit
def authenticate():
    print('Authenticating...')
    reddit = praw.Reddit('AnimeThemeBot', user_agent = 'Comments with link to anime op/ed as request, v0.1')
    print('Authenticated as {}'.format(reddit.user.me()))
    return reddit

# Get 25 comments and see if anyone requested an OP/ED using "!op" or "!ed"
def run_bot(reddit):
    # URLs for opening and endings go in these arrays
    openingArray = []
    endingArray = []
    commentReply = ''

    print('Obtaining 25 comments')
    for comment in reddit.subreddit('test').comments(limit=25):
        for match in re.finditer('!op\((.*)\)', comment.body, re.S):
            COMMENTS_DB_CURSOR.execute('SELECT id FROM comments WHERE id=?', [comment.id])
            if COMMENTS_DB_CURSOR.fetchone():
                continue
            replyToThis = comment
            add_comment_id(comment.id)
            # Fills the array with anime opening URLs
            for submission in reddit.subreddit('animethemes').search(match.group(1), 'new'):
                if submission.link_flair_text == 'Added to wiki' and '[OP]' in submission.title:
                     openingArray.append(submission)
            if not openingArray:
                print('Could not find any openings for this anime')
                return
            commentReply += 'Here are the openings I found for **{}'.format(match.group(1)) + '**'

            i = 0
            openingArray = list(reversed(openingArray))
            for url in openingArray:
                commentReply += '\n\n' + '[' + openingArray[i].title + '](' + openingArray[i].url + ')'
                i += 1
            commentReply += ('\n\n***    \n\n[Source](https://github.com/Knotts/AnimeThemeBot) \| Videos' +
                     ' taken from [/r/animethemes](https://reddit.com/r/animethemes) \| Programmed by /u/' +
                     'Knoticus')

            print('Replying to comment...')
            replyToThis.reply(commentReply)
            # print(commentReply)
            print('Reply completed, resting for 10 seconds...')
    time.sleep(10)

def add_comment_id(comment_id):
    COMMENTS_DB_CURSOR.execute('INSERT INTO comments VALUES (?, ?)', (comment_id, date.today()))
    COMMENTS_DB_CONN.commit()

def main():
    reddit = authenticate()
    while(True):
        run_bot(reddit)

if __name__ == '__main__':
    main()
