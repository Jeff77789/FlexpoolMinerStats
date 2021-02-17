# FlexpoolMinerStats
Stats monitoring, recording and charting for Flexpool Miners
By default, stats are saved to Google Sheets once every 5 minutes and when the script is first run

To start monitoring Flexpool stats, use the FlexpoolMinerStats.py file

![Miner stats screenshot](/Miner_stats.png)

Tested on Python 3.8.3 - Libraries required:
* flexpoolapi
* pygsheets
* cryptocompare
* time
* datetime

## Steps
1. Copy this Google sheet to your own Google Drive
https://docs.google.com/spreadsheets/d/1_Hyl4bFd4K2xdYm2YQf3VLd5xkLQiSOeGIJvJWyukyw/edit?usp=sharing

1. Create a new directory and download the FlexpoolMinerStats.py file to the directory

1. Go to the first sheet and copy the URL to your .py file (line 28)

1. Copy and insert your Flexpool Miner address to your code (line 18)

1. Follow the instructions here to download a client_secret.json file, put this in the same directory as your .py file (this is the trickest part)
https://pygsheets.readthedocs.io/en/stable/authorization.html

1. Running the script the first time, an authorization needs to be performed through Google following the link in the console

1. *Go to your Google Sheet to monitor stats*
    * Time
    * ETH Balance
    * ETH-USD Exchange Rate
    * USD Balance
    * 5 min USD change
    * 24 hour rolling difference
    * ETH 5 min change (typically block reward or payout)

1. A new row should be added to the Google Sheet every 5 minutes (9:30 AM, 9:35 AM, 9:40 AM, etc)


## Known Bugs
* Rolling 24h difference does not calculate correctly across payout periods
* Only works for 5 minute intervals, cell references need to be changed if shorter / longer intervals are used
* Update intervals less than 1 minute or >59 minutes not tested
