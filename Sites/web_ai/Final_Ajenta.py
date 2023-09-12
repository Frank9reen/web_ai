from Paragraf2 import get_text
from Parsing_Google import search_results
from Different_Paragraf import Agenta

search_query = 'уничтожение гнили на яблоне'
test_url_list = search_results(search_query, 'https://ferma.expert/')
print('3 ссылки после парсинга выдачи GOOGLE', test_url_list)


test_title_list = ['Свойства малины', 'Сорта малины с фото и описанием', 'Особенности дисхидии']

big_article_list = []
for i in test_url_list:
    big_article_list = big_article_list + get_text(i)  # объединили в один список

final_article_list = []
for k in test_title_list:
    for j in big_article_list:
        if k in j:
            # print(k, j)
            final_article_list.append(j)
print(final_article_list)