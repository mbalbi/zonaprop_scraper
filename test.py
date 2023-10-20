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
            'cookie': '_gcl_au=1.1.97044156.1697563643; sessionId=003ca1a9-c459-4002-884a-3b4f8b7c9d31; cf_clearance=GMNnjORgEXYTJHL5aOJcp7gnixX8QjsCc_XAcFVHYRQ-1697637485-0-1-2c0d1673.d22ee29b.9a977859-160.2.1697637485; _hjSessionUser_194887=eyJpZCI6IjllZDhiNzlhLTNiZjQtNTRkOC04MDMzLWJjNzllOTRkMDliMyIsImNyZWF0ZWQiOjE2OTc1NjM2NTEzMTUsImV4aXN0aW5nIjp0cnVlfQ==; __cf_bm=diYYBYxMaiErjQZKQB9Ak6E6C4I17D2SVFmOYSHgBzE-1697818421-0-AX/+d59Zktfc9I+nmnX6TNZVNx6Y031Zq1Wsa2AGB4J1a9lgCxA38b25atmzKtFM2giqrtaiRBCUNsBQw6x2E5Xes+nSwb+rfyoaptOPYksK; _gid=GA1.3.1580186032.1697818424; _hjIncludedInSessionSample_194887=0; _hjSession_194887=eyJpZCI6ImZkY2ZkZjE3LWZhZDAtNDM0NC1iZWJjLTlkY2QwZjdjNWNiYiIsImNyZWF0ZWQiOjE2OTc4MTg0MjU5NTksImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=; _hjAbsoluteSessionInProgress=0; g_state={"i_p":1697904913382,"i_l":2}; JSESSIONID=9EB2B1BB39EDB3C7155B80F40FD96082; _ga_68T3PL08E4=GS1.1.1697818424.3.1.1697818630.52.0.0; _ga=GA1.3.319898863.1697563644',
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
        print('Client error: ' + str(result.status_code))
        print(result.content)
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