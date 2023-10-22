# Import Python Libraries
# For HTML parsing
from bs4 import BeautifulSoup 
# For website connections
import requests 
import logging
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
from http.client import HTTPConnection


def get_headers():
    HTTPConnection.debuglevel = 1
    logging.basicConfig(level=logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
    #Headers
    headers={
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language':'es-ES,es;q=0.9,en;q=0.8,gl;q=0.7',
            'cache-control':'max-age=0',
            'sec-ch-ua':'"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'"Windows"',
            'sec-fetch-dest':'document',
            'sec-fetch-mode':'navigate',
            'sec-fetch-site':'none',
            'sec-fetch-user':'?1',
            'cookie':'_gcl_au=1.1.1721658168.1697564428; __rtbh.lid=^%^7B^%^22eventType^%^22^%^3A^%^22lid^%^22^%^2C^%^22id^%^22^%^3A^%^228kfp7t2kouPHdBWBUuSR^%^22^%^7D; sessionId=28f564e5-edb8-42ec-879c-e3acc15b504b; __rtbh.uid=^%^7B^%^22eventType^%^22^%^3A^%^22uid^%^22^%^7D; _fbp=fb.2.1697564429832.2532716; _hjSessionUser_194887=eyJpZCI6ImFmMmE3MWExLWZhNzEtNTU3Yy04YjVmLWJjODFhNGFiNDE1MyIsImNyZWF0ZWQiOjE2OTc1NjQ0Mjk5MTUsImV4aXN0aW5nIjp0cnVlfQ==; allowCookies=true; 52326857=visited; 52391660=visited; 52446284=visited; 51146304=visited; idUltimoAvisoVisto=51146304; 52444649=visited; g_state=^{^\^"i_p^\^":1698419957328,^\^"i_l^\^":3^}; __cf_bm=b3vsoEtajHgR1D2JPtcDvDSZ7bsQwCR50L7tNWypw_U-1698002953-0-AS55KHhbRTeSB2BPZV2CBUllH/ytBP7MQu1LGZgIrZv8KDKNcXXnLHypd9Bt7ILvQg5rbTU9HrptJBjRV24tmU+t79qcBYYLQtKxTQ9lqdfe; cf_clearance=c0YPiRJT7lxzuKr2YXNu_b9HVG4knASIBLpy0edNLqA-1698002954-0-1-3f9e9dc5.f03f67a9.77105ee-0.2.1698002954; _gid=GA1.3.735386245.1698002958; _dc_gtm_UA-5217585-1=1; __gads=ID=73a2ae1edaa1b7af:T=1697564426:RT=1698002955:S=ALNI_Mb2pzpcWx5CC9wOvwTkeskEAjy95A; __gpi=UID=00000a1fcf9fed0b:T=1697564426:RT=1698002955:S=ALNI_MYcW7BacbGkojtoQy8K9y7vO9cUkA; _gat_UA-5217585-1=1; JSESSIONID=C3E0A614AA9CB3A55568240F3CAF317A; _ga=GA1.3.508663498.1697564428; _ga_68T3PL08E4=GS1.1.1698002959.5.1.1698002965.54.0.0; _hjIncludedInSessionSample_194887=0; _hjSession_194887=eyJpZCI6IjAzNmNlMTdlLTA0N2EtNDgwMS1iOGQ0LWQ1MjYzNjVmOGMzZiIsImNyZWF0ZWQiOjE2OTgwMDI5NjkzODYsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=; _hjAbsoluteSessionInProgress=0"',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

    return headers

def get_page(city, type, beds, page):
  
    # url = f'https://www.torontorentals.com/{city}/{type}?beds={beds}%20&p={page}'
    # https://www.torontorentals.com/toronto/condos?beds=1%20&p=2
    url = f'https://www.zonaprop.com.ar/departamentos-alquiler.html'
    
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
        # print(result.headers)
        # print(result.content)
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