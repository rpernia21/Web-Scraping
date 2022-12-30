# -*- coding: utf-8 -*-
import pandas as pd
import re
import time
from bs4 import BeautifulSoup
import unicodecsv as csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



# open chrome drive
options = webdriver.ChromeOptions()
#options.add_argument("headless") # headless option
options.add_argument("--start-maximized")
browser = webdriver.Chrome("C:/Users/ipsas/Documents/Ronald Files/Python/Python Scripts/chromedriver.exe", chrome_options=options)
time.sleep(10)



with open("InquirerNet.csv", "wb") as fa:
    my_writer1 = csv.DictWriter(fa, fieldnames=("title", "url"))
    my_writer1.writeheader()

    for i in range(1,11):
        link = "https://www.inquirer.net/search/?q=populism#gsc.tab=0&gsc.q=populism&gsc.sort=&gsc.page=" + str(i)
        print("*****", i, "*****")
        
        browser.get(link)
        time.sleep(5)
        
        page = browser.execute_script("return document.body.innerHTML")
        soup = BeautifulSoup(page, "lxml")
        
        articles = soup.find_all("div", {"class":"gsc-webResult gsc-result"})
        len(articles)
        
        for ar in articles:
            title = ar.find_all("div", {"class":"gs-title"})[0].text
            url = ar.find_all("div", {"class":"gs-title"})[0].find_all("a")[0].get("href")
            print(title)
            
            my_writer1.writerow({"title":title, "url":url})
    
    
    
    