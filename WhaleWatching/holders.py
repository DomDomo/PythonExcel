import requests
from bs4 import BeautifulSoup
import json


def find_top_holders():

    print("Getting top 50 holders...")

    BASE_URL = "https://bscscan.com/"
    URL = BASE_URL + "token/generic-tokenholders2?m=normal&a=0xf09b7b6ba6dab7cccc3ae477a174b164c39f4c66&s=100000000000000000000000000&sid=2760e1b7d7cd4e69abe3df09a4bea20f&p=1"

    resp = requests.get(URL)
    sess = requests.Session()
    soup = BeautifulSoup(sess.get(URL).text, 'html.parser')


    holders = []

    for tr in soup.find("table", {"class": "table"}).find("tbody").find_all("tr"):
        stats = tr.find_all("td")

        holder = {
            "rank": stats[0].text,
            "address": stats[1].text,
            "link": BASE_URL + stats[1].find("a")['href'],
            "quantity": stats[2].text.split(".")[0],
            "percentage": stats[3].text,
            "old_quantity": stats[2].text.split(".")[0]
        }

        holders.append(holder)



    with open('holders.txt', 'w') as f:
        f.write(json.dumps(holders))

    print("Done.")

