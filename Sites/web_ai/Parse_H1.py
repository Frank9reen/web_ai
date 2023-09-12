from bs4 import BeautifulSoup
import requests

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
           'Accept': '*/*'}

def parse_h1(URL):
    r = requests.get(url=URL, headers=HEADERS)
    html = r.text
    soup = BeautifulSoup(html, "lxml")
    h1 = soup.h1.get_text()
    # print(h1)
    return h1
# parse_h1('https://migrantplanet.com/v-kakie-strany-mozhno-vyezzhat-sotrudnikam-fsb-spisok/')
