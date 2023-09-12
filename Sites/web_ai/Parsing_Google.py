import bs4
import requests
from bs4 import BeautifulSoup
from functools import reduce
# Делал по данному видео: https://www.youtube.com/watch?v=TddYMNVV14g
# https://console.cloud.google.com/
# from Paragraf2 import get_text


API_GOOGLE = 'AIzaSyBgPP2e6hwtwchSetnvoov0Yz4DcALgzjs'
SEARCH_ENGINE_ID = '82a35fa17037f41a4'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
           'Accept': '*/*'}

with open('Blocks_Urls.txt', 'r+') as file:
    block_list_urlz = file.readlines()
    block_list_urls = [(lambda i: i.replace('\n',''))(i) for i in block_list_urlz]
    # print('Блокированные на парсинг URLs --> ', block_list_urls)

def request_404(url):
    r = requests.get(url)
    return r.status_code

def how_many_h2(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, "lxml")
    count_h2 = len(soup.find_all("h2", soup))
    return count_h2

def how_many_content(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, "lxml")
    count_simbol = len(soup.body.get_text())
    return count_simbol

def search_results(search_query):
    links = []
    count = 2
    # block_list_urls = ['migrantplanet.com']
    # URL = 'https://www.gooleapis.com/customsearch/v1'
    URL = 'https://customsearch.googleapis.com/customsearch/v1'
    params = {
        'q': search_query,
        'key': API_GOOGLE,
        'cx': SEARCH_ENGINE_ID,
        # 'lr':'lang_uz',
        # 'gl':'UZ'
        # 'searchType':'image',
        # 'dateRestrict': '2021-01-01:2022-02-02',
        # 'fileType': 'pdf'
    }
    # Вывод 1-го линка
    responce = requests.get(URL, headers=HEADERS, params=params)
    resalts = responce.json()
    print(resalts)
    # r1 = resalts['items'][0]['link']
    # r2 = resalts['items'][1]['link']

    # links.append(urls_1)
    # links.append(r1)
    # links.append(r2)
    # print(links)

    block_d =[]
    with open("Block_domains.txt", 'r') as file:
        block_d = file.read().splitlines()
    # print('Загруженные домены из черного списка в лист: ', block_d)
    # block_d = ['ferma.expert', 'dacha.avgust.com','vgluhova.ru', 'ru.wikipedia.org']
    links = []
    i = 0


    for i in range(0, 10):
        print('счетчик ->', i)
        r = resalts['items'][i]['link']
        print('1111 ', r)
        r_cl = r.replace('https://', "").split('/')[0].replace("www.", "")
        print('чистый домен найденный ', r_cl)
        if r_cl in block_d :
            print('7777')
            pass
        elif request_404(r_cl) != '200':
            pass
        elif how_many_h2(r_cl) < 3:
            pass
        elif how_many_content(r_cl) < 3000:
            pass
        else:
            print(' --- ', r_cl, ' ---')
            links.append(r)
            print('сколько всего урлов сейчас добавил: ', len(links))

    while i < 9:
        print('счетчик ->', i)
        r = resalts['items'][i]['link']
        print('1111 ', r)
        r_cl = r.replace('https://', "").split('/')[0].replace("www.", "")
        print('чистый домен найденный ', r_cl)

        if r_cl in block_d :
            print('7777')
            pass
        elif request_404(r_cl) != '200':
            pass
        elif how_many_h2(r_cl) < 3:
            pass
        elif how_many_content(r_cl) < 3000:
            pass
        else:
            print(' --- ', r_cl, ' ---')
            links.append(r)
            print('сколько всего урлов сейчас добавил: ', len(links))

        if len(links) > 2:
            print('туууууууууууут')
            break
        i += 1
    print('Список урлов из Google: ', links)
    # Возвращает 3 urls
    return links

# --------------------------
search_query = 'уничтожение гнили на яблоне'
links_corts = search_results(search_query)
print('3 ссылки после парсинга выдачи GOOGLE', links_corts)

# u = how_many_content ('https://www.kp.ru/family/sad-i-ogorod/ukhod-za-malinoj-osenyu/?ysclid=lmaays58s8570226940')
# print(u)