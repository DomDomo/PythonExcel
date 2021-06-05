from bs4 import BeautifulSoup
from selenium import webdriver
from excel import save_to_excel
import requests
import os
import time
import re
import json
import glob
import settings


def find_top_holders():

    BASE_URL = settings.BASE_URL
    URL = settings.URL

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

    return holders

def import_old_holders():
    old_holders = []

    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, "old_holders")

    all_txts = sorted(glob.glob(path + '\*.txt'))
    filename = all_txts[0] if settings.USE_OLDEST else all_txts[-2]

    with open(filename, 'r') as f:
        old_holders = json.loads(f.read())

    return old_holders

def save_old_whales(holders):
    filename = "old_holders/old_holders" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, filename)
    with open(path, 'w') as f:
        f.write(json.dumps(holders))

def compare_holders(new_holders, old_holders):
    for new_holder in new_holders:
        for old_holder in old_holders:
            if new_holder["address"] == old_holder["address"]:
                new_holder["old_quantity"] = old_holder["quantity"]
                break

    return new_holders

def find_old_whale_balance(whale):
    URL = whale["link"]

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    time.sleep(settings.BSCSCAN_TIME_DELAY)

    soup = BeautifulSoup(driver.page_source,'html.parser')
    balance = soup.find("div", {"id": "ContentPlaceHolder1_divFilteredHolderBalance"}).text
    balance = balance.replace(",", "")
    # Find number in string
    number = int(re.findall('\d+', balance )[0])
    # Add commas to number
    number = '{:,}'.format(number)

    driver.quit()

    return number

def find_old_whales(new_holders, old_holders):
    new_addresses = [holder["address"] for holder in new_holders]
    old_adresses = [holder["address"] for holder in old_holders]

    new_whale_addresses = list(set(new_addresses) ^ set(old_adresses))
    old_whales = []

    for whale in new_whale_addresses:
        for holder in old_holders:
            if whale == holder["address"]:
                holder["old_quantity"] = holder["quantity"]
                holder["quantity"] = find_old_whale_balance(holder)
                old_whales.append(holder)
    

    return old_whales

def main():
    print("Getting top 50 holders...")
    holders = find_top_holders()

    old_holders = import_old_holders()

    print("Adding previous amount of tokens...")
    holders = compare_holders(holders, old_holders)

    if settings.SAVE_HOLDERS:
        save_old_whales(holders)

    print("Finding old whales...")
    old_whales = find_old_whales(holders, old_holders)

    if settings.REMOVE_DEAD_AND_PS:
        holders.pop(0)
        holders.pop(0)

    print("Making excel file...")
    save_to_excel(holders, old_whales)

if __name__ == "__main__":
    main()