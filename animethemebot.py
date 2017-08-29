# A Reddit bot that provides a user with the opening or ending theme song of an anime
# Created by Randy Chea (/u/Knoticus)
# License: MIT License

from bs4 import BeautifulSoup
from  urllib.parse import urlparse

import praw
import time
import re
import requests
import bs4

path = '/home/rchea/Projects/AnimeThemeBot/commented.txt'

def authentitcate()
    print('Authenticating...\n')
    reddit = praw.Reddit('AnimeThemeBot', user_agent='AnimeThemeBot user agent')
    print('Authenticated as {}\n'.format(reddit.user.me()))
    return reddit


