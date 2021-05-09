import os
import requests
from bs4 import BeautifulSoup
import time
import json
from datetime import datetime, timedelta

print("Getting CoinGecko data...")

def find_date(time):
    delta = ""
    if "days" in time:
        days = int(time.replace("days", "").strip())
        delta = timedelta(days=days)
    elif "hours" in time:
        hours = int(time.replace("hours", "").strip())
        delta = timedelta(hours=hours)
    return (datetime.date(datetime.now() - delta)).strftime("%Y-%m-%d")

cryptos = []
pages = 3
URL = "https://www.coingecko.com/en/coins/recently_added?page="

for page in range(pages):
    page_num = str(page+1)
    resp = requests.get(URL)
    sess = requests.Session()
    soup = BeautifulSoup(sess.get(URL + page_num).text, 'html.parser')

    print("Getting data from page {}".format(page_num))
    for tr in soup.find("tbody").find_all("tr"):
        name = tr.find("a", {"class": "tw-hidden"}).text.strip()
        time = tr.find("td", {"class": "trade"}).text.strip().replace('about', '')
        date = find_date(time)
        crypto = {
            "name": name,
            "time": time,
            "date": date
        }
        cryptos.append(crypto)

with open('CG.txt', 'w') as f:
    f.write(json.dumps(cryptos))

print("Done.")


