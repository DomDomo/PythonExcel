import os
import requests
from bs4 import BeautifulSoup
import time
import json

print("Getting CoinMarketCap data...")

URL = "https://coinmarketcap.com/new/"

cryptos = []

resp = requests.get(URL)
sess = requests.Session()
soup = BeautifulSoup(sess.get(URL).text, 'html.parser')

for tr in soup.find("tbody").find_all("tr"):
    name = tr.find("p", attrs={"color": "text"}).text
    time = tr.find_all("td")[-2].text.replace('ago', '')

    crypto = {
        "name": name,
        "time": time
    }
    cryptos.append(crypto)

with open('CMC.txt', 'w') as f:
    f.write(json.dumps(cryptos))

print("Done.")

