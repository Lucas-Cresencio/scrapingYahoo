# WebScraping Yahoo Finance website.
import time
import webbrowser

import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

from selenium.webdriver.common.by import By


def getStock(region):

    region = region

    url = "https://finance.yahoo.com/screener/new"

    option = webdriver.ChromeOptions()

    # To not open Windows Defender
    option.add_argument('disable-infobars')
    option.add_argument('user-data-dir=C:\python27\profile')

    option.headless = True
    driver = webdriver.Chrome(r"C:\Users\lucas\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get(url)

    driver.find_element_by_xpath("//*[@id='screener-criteria']/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[1]/button").click()
    driver.find_element_by_xpath("//*[@id='screener-criteria']/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li/div/div/span/span").click()
    time.sleep(2)

    # Select region
    for x in range(1, 57):
        varRegion = driver.find_element_by_xpath("//*[@id='dropdown-menu']/div/div[2]/ul/li[%s]/label/span" % x).text
        if varRegion in region:
            driver.find_element_by_xpath("//*[@id='dropdown-menu']/div/div[2]/ul/li[%s]/label/span" % x).click()
            break
        else:
            continue

    # Find stocks
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='screener-criteria']/div[2]/div[1]/div[3]/button[1]").click()
    time.sleep(2)

    # Get table with stocks
    elementStocks = driver. find_element_by_xpath("//*[@id='scr-res-table']/div[1]/table")
    html_content = elementStocks.get_attribute('outerHTML')

    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    # Data Structure Conversion
    df_full = pd.read_html(str(table))[0].head(time.sleep(187.8))
    df = df_full[['Symbol', 'Name', 'Price (Intraday)']]


    # Convert to Dict
    list = {}
    list['Stocks'] = df.to_dict('records')

    # Convert to JSON
    js = json.dumps(list)
    fp = open('stocks.json', 'w')
    fp.write(js)
    fp.close()

    driver.quit()

    return js




