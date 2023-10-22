import pycurl
import certifi
from io import BytesIO
# Creating a buffer as the cURL is not allocating a buffer for the network response
buffer = BytesIO()
c = pycurl.Curl()
#initializing the request URL
c.setopt(c.URL, 'https://www.zonaprop.com.ar/departamentos-alquiler-capital-federal.html')
# Header
custom_headers = ['authority:www.zonaprop.com.ar',
        'accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language:es-ES,es;q=0.9,en;q=0.8,gl;q=0.7',
            'cache-control:max-age=0',
            'sec-ch-ua:"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile:?0',
            'sec-ch-ua-platform:"macOS"',
            'sec-fetch-dest:document',
            'sec-fetch-mode:navigate',
            'sec-fetch-site:cross-site',
            'sec-fetch-user:?1',
            'cookie: _gcl_au=1.1.1721658168.1697564428; __rtbh.lid=^%^7B^%^22eventType^%^22^%^3A^%^22lid^%^22^%^2C^%^22id^%^22^%^3A^%^228kfp7t2kouPHdBWBUuSR^%^22^%^7D; sessionId=28f564e5-edb8-42ec-879c-e3acc15b504b; __rtbh.uid=^%^7B^%^22eventType^%^22^%^3A^%^22uid^%^22^%^7D; _fbp=fb.2.1697564429832.2532716; _hjSessionUser_194887=eyJpZCI6ImFmMmE3MWExLWZhNzEtNTU3Yy04YjVmLWJjODFhNGFiNDE1MyIsImNyZWF0ZWQiOjE2OTc1NjQ0Mjk5MTUsImV4aXN0aW5nIjp0cnVlfQ==; allowCookies=true; 52326857=visited; 52391660=visited; 52446284=visited; 51146304=visited; idUltimoAvisoVisto=51146304; 52444649=visited; g_state=^{^\^"i_p^\^":1698419957328,^\^"i_l^\^":3^}; __cf_bm=b3vsoEtajHgR1D2JPtcDvDSZ7bsQwCR50L7tNWypw_U-1698002953-0-AS55KHhbRTeSB2BPZV2CBUllH/ytBP7MQu1LGZgIrZv8KDKNcXXnLHypd9Bt7ILvQg5rbTU9HrptJBjRV24tmU+t79qcBYYLQtKxTQ9lqdfe; cf_clearance=c0YPiRJT7lxzuKr2YXNu_b9HVG4knASIBLpy0edNLqA-1698002954-0-1-3f9e9dc5.f03f67a9.77105ee-0.2.1698002954; _gid=GA1.3.735386245.1698002958; _dc_gtm_UA-5217585-1=1; __gads=ID=73a2ae1edaa1b7af:T=1697564426:RT=1698002955:S=ALNI_Mb2pzpcWx5CC9wOvwTkeskEAjy95A; __gpi=UID=00000a1fcf9fed0b:T=1697564426:RT=1698002955:S=ALNI_MYcW7BacbGkojtoQy8K9y7vO9cUkA; _gat_UA-5217585-1=1; JSESSIONID=C3E0A614AA9CB3A55568240F3CAF317A; _ga=GA1.3.508663498.1697564428; _ga_68T3PL08E4=GS1.1.1698002959.5.1.1698002965.54.0.0; _hjIncludedInSessionSample_194887=0; _hjSession_194887=eyJpZCI6IjAzNmNlMTdlLTA0N2EtNDgwMS1iOGQ0LWQ1MjYzNjVmOGMzZiIsImNyZWF0ZWQiOjE2OTgwMDI5NjkzODYsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=; _hjAbsoluteSessionInProgress=0"',
            'upgrade-insecure-requests:1',
            'user-agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36']
c.setopt(pycurl.HTTPHEADER, custom_headers)
#setting options for cURL transfer  
c.setopt(c.WRITEDATA, buffer)
#setting the file name holding the certificates
c.setopt(c.CAINFO, certifi.where())
# perform file transfer
c.perform()
#Ending the session and freeing the resources
c.close()

#retrieve the content BytesIO
body = buffer.getvalue()
#decoding the buffer 
print(body.decode('iso-8859-1'))
