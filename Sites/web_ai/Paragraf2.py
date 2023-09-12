# Создание списка кортежей

import requests
from bs4 import BeautifulSoup
import lxml
import unicodedata
# from GPT3_openai_4 import Chat_converstaion

def get_text(url):    # return clear text of article
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
               'Accept': '*/*'}
    r = requests.get(url, headers=HEADERS).text
    soup0 = BeautifulSoup(r, 'html.parser')
    soupb = soup0.body  # взяли только бади
    content = soupb.find_all(['h2', 'p', 'img'])  # взяли тэги h2 и p
    # print(content)
    abzac_str = ''
    img_str = ''
    h2 = 'Google'
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
            img_str = str(p)
            img_str = img_str + ' '
        elif p.name == 'p':
            # abzac_str = unicodedata.normalize("NFKD", abzac_str)
            abzac_str = abzac_str.replace(u'\n', '')
            abzac_str = abzac_str.replace(u'\xa0', '')
            abzac_str = abzac_str.replace(u'\r', '')
            abzac_str = abzac_str.replace(u'\t', '')

            abzac_str = abzac_str + p.text + ' '
    # print(all_article_list)

    return all_article_list


# def wrap_tag(text):
#     t1 = text.splitlines()
#     for t in t1:
#         if t == '':
#             t1.remove(t)
#     # print(t1)
#     text_tag = ''
#     for tt in t1:
#         wrap_text = '<p>' + tt + '</p>'
#         text_tag = text_tag + wrap_text
#     return text_tag

# --------------------------
# b = []
url = 'https://ferma.expert/rasteniya/ovoshchi/luk/posadka-luka-vesnoy/'
lsst = get_text(url)
print(lsst)
# # b = *lsst
# # print(*lsst)
#
