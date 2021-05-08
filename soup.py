print("hello")

import os
import requests
from bs4 import BeautifulSoup
import time

URL = "https://bscscan.com/token/generic-tokenholders2?a=0xf09b7b6ba6dab7cccc3ae477a174b164c39f4c66&s=0&p=1"

resp = requests.get(URL)
sess = requests.Session()
soup = BeautifulSoup(sess.get(URL).text, 'html.parser')

print(soup.find_all("span", {"class": "hidden-xs"})[0].text)

