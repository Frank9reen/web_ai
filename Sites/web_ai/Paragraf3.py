# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
import unicodedata


def merge_4_links(urls: list) -> list:
    big_article_list = []
    for url in urls:
        big_article_list = big_article_list + get_h2_text_image(url)
    return big_article_list


def get_h2_text_image(url):    # return clear text of article
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
               'Accept': '*/*'}
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'

    # print('************ ',r.text)
    soup0 = BeautifulSoup(r.text, 'lxml')
    soupb = soup0.body  # взяли только бади
    content = soupb.find_all(['h2', 'p', 'img'])  # взяли тэги h2 и p
    # print(content)
    abzac_str = ''
    img_str = ''
    h2 = 'Нет заголовка'  # изменил с None
    all_article_list = []
    for p in content:
        # print(p.text)  # список всего текста
        h2_abzac_tuple = (h2, abzac_str, img_str)
        if p.name == 'h2':
            all_article_list.append(h2_abzac_tuple)

            h2 = p.text
            abzac_str = ''
            img_str = ''
        elif p.name == 'img':
            # img_str = str(p)
            img_str = p['src']
            # вот тут функция очистки тэгов с картинкой нужна
        elif p.name == 'p':
            abzac_str = abzac_str.replace(u'\n', '')
            abzac_str = abzac_str.replace(u'\xa0', ' ')
            abzac_str = abzac_str.replace(u'\r', '')
            abzac_str = abzac_str.replace(u'\t', '')
            abzac_str = abzac_str + p.text + ' '
    # print(all_article_list)
    return all_article_list


s = ['https://ferma.expert/rasteniya/kustarniki/smorodina/krasnaya-saharnaya/', 'https://floristics.info/ru/stati/sad/2651-krasnaya-smorodina-posadka-i-ukhod-obrezka-i-razmnozhenie.html', 'https://kfh-fruktovyjsad.ru/catalog/yagodnyie-kustarniki/smorodina/krasnaya/saharnaya', 'https://terra29.ru/products/smorodina-krasnaya-saharnaya']
merge_4_links(s)
