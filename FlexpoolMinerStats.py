import time
from datetime import datetime, timedelta

import flexpoolapi
import pygsheets

import cryptocompare

# ETH Price
# cryptocompare.get_price('ETH', curr='USD', full=True, exchange='Coinbase')
# Pool
# flexpoolapi.pool.hashrate()
# flexpoolapi.pool.miners_online()
# flexpoolapi.pool.workers_online()

# Miner
# TODO Replace with your miner address here:
miner = flexpoolapi.miner("0x5400c6A42F522ed2F996F25dD468d6d70e065035")

# Initialize Google Sheets
# TODO Follow the instructions here to download a client_secret.json file
# (Enable the Google Drive API and the Google Sheets API for your Google developer account and create a OAuth 2.0 Client ID on Google API with type "Desktop")
# https://pygsheets.readthedocs.io/en/stable/authorization.html
client = pygsheets.authorize()
# TODO Look at the console window, follow the link and authorize the authentication (first time only)

# TODO Replace with your Google Sheet url here:
sh = client.open_by_url("https://docs.google.com/spreadsheets/d/1_Hyl4bFd4K2xdYm2YQf3VLd5xkLQiSOeGIJvJWyukyw/edit#gid=1648906181")
wks = sh.sheet1  # Save data in Sheet 1 or the first sheet

# Find time interval until next round minute
def get_sleep_time(interval_minutes=1):
    now = datetime.now()
    next_run = now.replace(minute=int(now.minute / interval_minutes) * interval_minutes, second=0, microsecond=0) + timedelta(minutes=interval_minutes)
    return (next_run - now).total_seconds()

def miner_monitor(interval_minutes=5):
    while True:
        now = datetime.now()
        current_time = now.strftime("%m/%d/%Y %H:%M:%S")
        print(f"\nCurrent Time = {current_time}\n")

        # Save Miner balance to Google Sheets
        ETH_price = cryptocompare.get_price('ETH', currency='USD')
        print(f"Current ETH price: {ETH_price['ETH']['USD']} USD")
        flex_balance = miner.balance()
        wks.insert_rows(1, 1, None, False)
        wks.update_value((2, 1), current_time)  # (1,1) is also A1
        wks.update_value((2, 2), flex_balance)  # (1,1) is also A1
        wks.update_value((2, 3), flex_balance / 1e18, True)
        wks.update_value((2, 4), ETH_price['ETH']['USD'], True)
        wks.update_value((2, 5), flex_balance / 1e18 * ETH_price['ETH']['USD'], True)
        wks.update_value((2, 6), "=E2-E3")  # Difference from previous cell
        wks.update_value((2, 7), "=E2-E289")  # 24 hour rolling revenue based on 5 min intervals
        wks.update_value((2, 8), "=IF(C2-C3<>0,C2-C3,)")  # ETH Difference for blocks and payouts

        sleep_time = get_sleep_time(interval_minutes)
        print(f"{sleep_time:0.4} seconds until next run")
        # time.sleep(10)  # testing
        time.sleep(sleep_time)  # testing

if __name__ == "__main__":
    # Wrap miner_monitor() in a while loop with try & except to keep running when errors are encountered
    while True:
        try:
            miner_monitor(5)
        except:
            pass
        time.sleep(15)
