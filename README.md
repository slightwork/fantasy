# Fantasy Football
Fantasy League Toolkit Generator for ESPN Leagues

## Changes from the original
1. This forked repo focuses on leagues where decimal (or floating) point scoring is used.
2. The database schema has been modified from the [original](https://github.com/jpmayer/fantasy) to support decimal scoring.
3. __NOTE__: This repo assumes you have familiarity with the [original](https://github.com/jpmayer/fantasy) project already.
4. We don't use home field advantages at all, so...yeah.

[reddit Tutorial Page](https://www.reddit.com/r/fantasyfootball/comments/526bhh/espn_leagues_add_nice_looking_htmlcss_power/)



## CLI commands:
> * python parseOldYear.py [year] > [filename]
> * *Example*: python parseOldYear.py 2013 > temp.txt

> * python parseYear.py [year] > [filename]
> * *Example:* python parseYear.py 2015 > temp.txt

> * python allTimeWins.py

> * python recordBook.py

> * python powerRanking.py

> * python powerRanking.py [filename]
> * *Example:* python powerRanking.py preseason.txt

> * python parseWeek.py [filename]
> * python parseWeek.py weekOne2016.txt
