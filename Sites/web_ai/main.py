import threading

from Parsing_all_page import call_parsing
# from parsing.take_url import take_url
from Parse_H1 import parse_h1
# from Parsing_Google import search_results
import os
from Paragraf3 import merge_4_links
from Different_Paragraf import agenta
from Parsing_Google2 import parsing_google
from GPT3_openai_4 import Chat_converstaion, results
import time
from threading import Thread
from operator import itemgetter
import random
from Wrap_text import wrap_tags
import pandas as pd
from get_in_excel import get_in_excel


domain = 'https://ferma.expert'  # название сайта на основе которого мы хотим сделать ai-сайт
domain2 = domain.split('://')[1]
if domain2 in os.listdir(path='urls'):
    print('уже спарсили урлы сайта')
else:
    call_parsing(domain)  # Парсинг всех урлов по названию домена (domain) в папку urls

with open('urls/'+domain2, 'r') as file:
    urls_list = file.read().splitlines()  # список всех урлов по домену

for url_1 in urls_list[6:7]:  # Иду по urls сайта беру первый урл в списке всех урлов сайта
    try:
        h1 = parse_h1(url_1)  # Парсинг H1 текущего урла, если ошибка то следующий url
        links_4_g = parsing_google(h1)
        print('*****', links_4_g)
        ls = merge_4_links(links_4_g)  # !функция объединения 4х ссылок в кортежный список - большая статья

        #  Получили список кортежей -> Необходимо взять и сделать список Н2  -> Отправить в Дифферентатор и Кластеризатор- >
        list_h2 = [i for i, *j in ls]
        print('*** ', list_h2)
        h2_new = agenta(list_h2)     # -> получили список  очищенныый и кластеризованный
        print(h2_new)
        h2_text_img_new = [(h, t, p) for h, t, p in ls if h in h2_new]
        print('ДЛИНА -->', len(h2_text_img_new))
        i = 0
        for hti in h2_text_img_new:
            i = i + 1
            print(i, '----------', hti)

        h2_t_img_new_after_gpt3 = []
        tuple = ()
        all_text = ''
        # Делаем список из подзаголовков
        tt = [tt for h, tt, img in h2_text_img_new]
        start_time = time.time()

        # Создаем и запускаем потоки
        threads = []
        for i in range(0, len(tt)):
            h2 = h2_text_img_new[i][0]
            img = h2_text_img_new[i][2]
            trr = Thread(target=Chat_converstaion, args=(tt[i], 'text_2_pr', i, h2, img), daemon=False)
            trr.start()
            threads.append(trr)
            tt.append(trr)
        for thread in threads:
            print('Блокировка потока', thread.name)
            thread.join()

        # Сортировка списка кортежей текстов по GPT-3
        results.sort(key=lambda x: x[0])

        for r in results:  # список кортежей
            print('ПОШАГОВЫЙ ИТОГ:', r)

        get_in_excel(results)

        # html = ''
        # for id, h, t, i in results:
        #     html = html + '<h2>'+ h + '</h2>'+ '\n' + wrap_tags(t)
        # print(html)
        # end_time = time.time()
        # print('Время на создание сатьи', end_time - start_time)

    except:
        continue



