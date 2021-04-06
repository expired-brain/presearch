#   Copyright (c) 2021.
#   Version : 0.0.1
#   Script Author : Sushen Biswas
#
#   Sushen Biswas Github Link : https://github.com/sushen
#
#   !/usr/bin/env python
#   coding: utf-8

import time
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from random_words import RandomWords

# for MacOS
from webdriver_manager.chrome import ChromeDriverManager

# TODO: 3 Make a Long List of keyword

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--incognito")

'''
TODO:
    - different module for cross platform
    -
'''


def driver_for_mac():
    return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


def driver_for_windows():
    return webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)


# driver = driver_for_windows()
driver = driver_for_mac()
chrome_options.add_argument("user-data-dir=chrome-data")
driver.implicitly_wait(25)  # seconds

# What will be searched
driver.get("https://engine.presearch.org")

# TODO: 2 Make a login strong system in environment veriable
print(input("Enter your Username and Password Menually then enter 1 : "))

# Search using preserch google extension url
rw = RandomWords()
count = 0
while True:
    if count == 15:
        count = 0
        print("sleeping for 2 min.")
        time.sleep(125)
    count += 1
    time.sleep(randint(3, 8))
    url = f"https://presearch.org/extsearch?term={rw.random_word()}"
    print(count, time.strftime("%H:%M:%S"), url)
    driver.get(url)
