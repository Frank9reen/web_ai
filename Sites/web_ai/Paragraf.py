import requests
from bs4 import BeautifulSoup
import lxml
import unicodedata
from GPT3_openai_4 import Chat_converstaion

def get_text(url):    # return clear text of article
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
               'Accept': '*/*'}
    r = requests.get(url, headers=HEADERS).text
    soup0 = BeautifulSoup(r, 'lxml')
    soupb = soup0.body  # взяли только бади
    content = soupb.find_all(['h2', 'p', 'img'])  # взяли тэги h2 и p
    # print(content)
    abzac_str = ''
    h2 = None
    all_article_list = []
    for p in content:
        # print(p.text)  # список всего текста
        h2_abzac_tuple = (h2, abzac_str)
        if p.name == 'h2':
            all_article_list.append(h2_abzac_tuple)
            h2 = p.text
            abzac_str = ''
        # elif p.name == 'img':
        #     img_str = str(p)
        #     abzac_str = abzac_str + img_str + ' '
        elif p.name == 'p':
            # abzac_str = unicodedata.normalize("NFKD", abzac_str)
            abzac_str = abzac_str.replace(u'\n', '')
            abzac_str = abzac_str.replace(u'\xa0', '')
            abzac_str = abzac_str.replace(u'\r', '')

            abzac_str = abzac_str + p.text + ' '
    print(all_article_list)
    return all_article_list


def wrap_tag(text):
    t1 = text.splitlines()
    for t in t1:
        if t == '':
            t1.remove(t)
    # print(t1)
    text_tag = ''
    for tt in t1:
        wrap_text = '<p>' + tt + '</p>'
        text_tag = text_tag + wrap_text
    return text_tag

# --------------------------
url = 'https://ferma.expert/rasteniya/ovoshchi/luk/posadka-luka-vesnoy/'
lsst = get_text(url)
#
text_new = ''
new = ''
count = 0
i = 0
for h2, text in lsst:
    count = count + 1
    text_new = text_new + new
    # print(text)
    query_type = 'text_2_pr'
    # new = Chat_converstaion(text, query_type)
    if i == 2:
        query_type = 'text_2_pr_7_spiski'
        new = f'<h2>{h2}</h2>\n {Chat_converstaion(text, query_type)}\n'
    else:
        if h2 != None:
            new = f"<h2>{h2}</h2>\n {Chat_converstaion(text, query_type)} \n"
        else:
            pass

    i = i + 1
    print(new)

print('ITOG ---->    ', text_new)
#------------------------
text = """
Весенняя посадка лука является эффективным способом получить обильный урожай осенью. Она позволяет растению развиться и сформировать луковицы достаточно рано, что предоставляет возможность получить ранний урожай. Однако для достижения успешных результатов необходимо знать правильные сроки посевных работ и организовать грамотный уход за растениями.

Определение оптимального времени для весенней посадки лука является важным аспектом. Ведь выбор сроков зависит от климатических условий и региона. Рекомендуется сажать лук, когда почва прогреется до 5-10 градусов Цельсия. Это позволит растениям укорениться и начать активно развиваться. 

При выборе сорта лука также следует учитывать особенности конкретного региона. Некоторые сорта могут лучше адаптироваться к местным условиям, что способствует более успешному выращиванию растений. 

Кроме того, грамотный уход за посаженным луком также играет важную роль. Регулярное поливание, подкормка и защита от вредителей и болезней следует стать основными мероприятиями. Это поможет растениям поддерживать оптимальные условия для роста и развития. 

Для повышения урожайности лука важно обеспечить растениям достаточно места для роста и развития. Прореживание станет полезным инструментом, который позволит растениям иметь достаточно места для развития и увеличить количество луковиц. 

Все эти уточняющие мысли и факты являются важными дополнениями к основным ключевым идеям. Они помогут обогатить информацию, сделать статью более полезной и интересной для читателей, а также передать им все необходимые знания для успешной посадки и выращивания лука.

"""
