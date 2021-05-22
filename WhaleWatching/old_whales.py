from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re

whale = {'rank': '50', 'address': '0x505dd22c1bacced7531f319f5008318a440490bc', 'link': 'https://bscscan.com//token/0xf09b7b6ba6dab7cccc3ae477a174b164c39f4c66?a=0x505dd22c1bacced7531f319f5008318a440490bc', 'quantity': 9, 'percentage': '0.0950% ', 'old_quantity': '95,004,246,973,923'}

def find_old_whale_balance(whale):
    URL = whale["link"]

    driver = webdriver.Chrome()
    driver.get(URL)
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source,'html.parser')
    balance = soup.find("div", {"id": "ContentPlaceHolder1_divFilteredHolderBalance"}).text
    balance = balance.replace(",", "")
    # Find number in string
    number = int(re.findall('\d+', balance )[0])
    # Add commas to number
    number = '{:,}'.format(number)

    driver.quit()

    return number

find_old_whale_balance(whale)

