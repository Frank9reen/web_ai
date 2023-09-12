import pandas as pd
import re
import requests
import base64
import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup


# в цикл надо поставить, чтобы перебор был
def take_url_img_in_wp(list_test: list) -> list:  # работает на урлах коротких
    img_url_in_wp_list = []
    for i in list_test:
        url_img = i
        a = urlparse(url_img)
        name_img = os.path.basename(a.path)  # Output: 09-09-201315-47-571378756077.jpg
        print(name_img)

        img_data = requests.get(url_img).content  # скачиваем миниатюру с сайта и добавляем к себе в медиабиблиотеку WP
        with open(f'pictures/{name_img}', 'wb') as f:  # сохранили у себя на компьютере
            f.write(img_data)

        url = "https://supergardener.ru/wp-json/wp/v2/"
        user = "superg"
        password = "ZkYn CSVh RFku gx1T KOIF Hank"
        credentials = user + ':' + password
        token = base64.b64encode(credentials.encode())
        header = {'Authorization': 'Basic ' + token.decode('utf-8')}
        # date = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime())
        # print('Ответ сервера', requests.get(url).status_code)
        media = {'file': open(f'pictures/{name_img}', 'rb'),  # открыли миниатюру на компьютере
                 'caption': 'pic'}
        responce_media = requests.post(url + 'media', headers=header, files=media)
        img_url_in_wp = responce_media.json()['guid']['rendered']  # ссылка в ВП на картинку

    img_url_in_wp_list.append(img_url_in_wp)

    return img_url_in_wp_list


def replace_urls_in_excel():  # не работает на урлах коротких
    # test_str = '<img alt="" class="aligncenter wp-image-22715 size-full" data-src="https://countryhouse.pro/wp-content/uploads/2018/07/Peresadka-kusta-smorodiny-letom.jpg" height="450" sizes="(max-width: 600px) 100vw, 600px" srcset="https://countryhouse.pro/wp-content/uploads/2018/07/Peresadka-kusta-smorodiny-letom.jpg 600w, https://countryhouse.pro/wp-content/uploads/2018/07/Peresadka-kusta-smorodiny-letom-300x225.jpg 300w, https://countryhouse.pro/wp-content/uploads/2018/07/Peresadka-kusta-smorodiny-letom-86x64.jpg 86w" width="600"/> '
    data = pd.read_excel('test.xlsx')
    # print(data)
    url_text_list = []
    for i in data[3]:  # список грязных урлов в эксель файле
        soup = BeautifulSoup(i, "html.parser")  # ошибка есть тэг src / data-src
        try:
            s = soup.find('img')['src']
            print(i, s)
        except:
            s = soup.find('img')['data-src']
            print(i, s)
        only_link = re.search("(?P<url>src?://[^\s]+)", i)
        # print(only_link)
        # only_link = re.search("(?P<url>https?://[^\s]+)", i).group("url")
        url_text_list.append(only_link)
    # print(url_text_list)
    # take_url_img_in_wp(url_text_list)  # функция
    return

replace_urls_in_excel()

# data2 = pd.DataFrame(url_text_list)
# data[3] = data2  # заменили столбец на ссылки
# # print(data)
# # data.to_excel('test-img-urls.xlsx')


# print(take_url_img_in_wp(['https://countryhouse.pro/wp-content/uploads/2018/07/Peresadka-kusta-smorodiny-letom.jpg']))


