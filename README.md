# AnimeThemeBot
A reddit bot that provides theme songs of animes as requested.

## How it works
This bot utilizes PRAW, a python wrapped for Reddit's API, in order to retreieve comments and review its contents. If the comment contains "!op('title')" or "!ed('title')", it will retreieve all relevant theme songs from the subrebbit /r/AnimeThemes, based on the type of request they made. "!op" is used for opening credits while "!ed" is used for ending credits.

## Example
https://i.imgur.com/yVdd6U9.png

## TODO:
- Multiple requests in one comment
- EDs
- Cleaner comment formatting
