from Paragraf2 import get_text
from Different_Paragraf import Agenta
test_url_list = ['https://rastenievod.com/dishidiya.html', 'https://rastenievod.com/malina.html', 'https://rastenievod.com/darlingtoniya.html'  ]


def h2_form(test_url_list):
    big_article_list = []
    list_h2 = []
    for i in test_url_list:
        big_article_list = big_article_list + get_text(i)  # объединили в один список
    for i in  big_article_list:
        list_h2.append(i[0])
    return list_h2


print(h2_form(test_url_list))
all_list_h2 = h2_form(test_url_list)

s = Agenta(all_list_h2)
print(s)
