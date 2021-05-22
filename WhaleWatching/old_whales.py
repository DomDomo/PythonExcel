from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re

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