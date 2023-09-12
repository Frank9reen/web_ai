# работает выдача 10 урлов яндекса/ google по запросу
import requests
import xmltodict
from bs4 import BeautifulSoup


def check_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0', 'Accept': '*/*'}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return False
    soup = BeautifulSoup(r.text, 'html.parser')
    count_h2 = len(soup.find_all('h2'))
    count_symbols = len(soup.body.get_text())
    if count_symbols < 5000:
        return False
    if count_h2 < 4:
        return False
    return True


def parsing_google(search_response: str) -> list:
    headers = {'Content-Type': 'application/xml'}
    resp = requests.get(f"http://xmlriver.com/search/xml?user=10523&key=aaac4e5ac50226e36818e376b4d8a9898dac9b57&query={search_response}", headers=headers)
    dict_data = xmltodict.parse(resp.content)
    list_urls = []
    for i in dict_data['yandexsearch']['response']['results']['grouping']['group']:
        el = i['doc']['url']
        try:
            if check_url(el) == False:
                pass
            else:
                list_urls.append(el)  # последний элемент содержит None
        except:
            pass
    return list_urls[:3]


def parsing_yandex(search_response: str) -> list:
    headers = {'Content-Type': 'application/xml'}
    resp = requests.get(f"http://xmlriver.com/search_yandex/xml?user=10523&key=aaac4e5ac50226e36818e376b4d8a9898dac9b57&query={search_response}", headers=headers)
    dict_data = xmltodict.parse(resp.content)

    if KeyError or RuntimeError or TypeError:
        print('Ошибка с парсингом')
    else:
        list_urls = []
        for i in dict_data['yandexsearch']['response']['results']['grouping']['group']:
            el = i['doc']['url']
            list_urls.append(el)
    return list_urls[:3]


# print(check_url('https://agro-him.com.ua/index.php?route=information/news/news&news_id=8'))
# print(parsing_google('гниль малины'))
# # print(parsing_yandex('гниль малины'))