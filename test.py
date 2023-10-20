# Import Python Libraries
# For HTML parsing
from bs4 import BeautifulSoup 
# For website connections
import requests 
# To prevent overwhelming the server between connections
from time import sleep 

# Display the progress bar
from tqdm import tqdm
# For data wrangling
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# For creating plots
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def get_headers():
    #Headers
    headers={'authority':'www.zonaprop.com.ar',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language':'es-ES,es;q=0.9,en;q=0.8,gl;q=0.7',
            'cache-control':'max-age=0',
            'sec-ch-ua':'"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'"macOS"',
            'sec-fetch-dest':'document',
            'sec-fetch-mode':'navigate',
            'sec-fetch-site':'cross-site',
            'sec-fetch-user':'?1',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

    return headers

def get_page(city, type, beds, page):
  
    # url = f'https://www.torontorentals.com/{city}/{type}?beds={beds}%20&p={page}'
    # https://www.torontorentals.com/toronto/condos?beds=1%20&p=2
    url = f'https://www.zonaprop.com.ar/departamentos-alquiler-capital-federal.html'
    
    # headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',  }
 
    result = requests.get(url, headers=get_headers())
    
    # check HTTP response status codes to find if HTTP request has been successfully completed
    if result.status_code >= 100  and result.status_code <= 199:
        print('Informational response')
    if result.status_code >= 200  and result.status_code <= 299:
        print('Successful response')
        soup = BeautifulSoup(result.content, "lxml")
    if result.status_code >= 300  and result.status_code <= 399:
        print('Redirect')
    if result.status_code >= 400  and result.status_code <= 499:
        print('Client error')
    if result.status_code >= 500  and result.status_code <= 599:
        print('Server error')
        
    return soup

# Loop through pages
for page_num in tqdm(range(1, 250)):
    sleep(2)
    
    # get soup object of the page
    soup_page = get_page('toronto', 'condos', '1', page_num)

    # grab listing street
    for tag in soup_page.find_all('div', class_='listing-brief'):
        for tag2 in tag.find_all('span', class_='replace street'):
            # to check if data point is missing
            if not tag2.get_text(strip=True):
                listingStreet.append("empty")
            else:
                listingStreet.append(tag2.get_text(strip=True))