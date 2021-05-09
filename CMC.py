import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta

print("Getting CoinMarketCap data...")

def find_date(time):
    delta = ""
    if "Today" in time:
        delta = timedelta(days=0)
    elif "day" in time:
        days = int(time.split(" ")[0])
        delta = timedelta(days=days)
    return (datetime.date(datetime.now() - delta)).strftime("%Y-%m-%d")

URL = "https://coinmarketcap.com/new/"

cryptos = []

resp = requests.get(URL)
sess = requests.Session()
soup = BeautifulSoup(sess.get(URL).text, 'html.parser')

for tr in soup.find("tbody").find_all("tr"):
    name = tr.find("p", attrs={"color": "text"}).text
    time = tr.find_all("td")[-2].text.replace('ago', '')
    date = find_date(time)

    crypto = {
        "name": name,
        "time": time,
        "date": date
    }
    cryptos.append(crypto)

print("Adding outdated cryptos to CMC list...")
prev_cryptos = []

with open('CMC.txt', 'r') as f:
    prev_cryptos = json.loads(f.read())

old_cryptos = []

while(cryptos[-1]["name"] != prev_cryptos[-1]["name"]):
    prev_cryptos[-1]["time"] = "outdated"
    old_cryptos.append(prev_cryptos[-1])
    prev_cryptos.pop(-1)

cryptos = cryptos + old_cryptos

print("Writing data to text file")
with open('CMC.txt', 'w') as f:
    f.write(json.dumps(cryptos))

print("Done.")

# Last one was WSTA Wrapped Statera

