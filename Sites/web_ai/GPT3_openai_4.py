# Создание нового текста от вопроса в OPENAI
import openai
import os
import time
import random
from Wrap_text import wrap_tags
# openai.api_key = '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'
openai.api_key = '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'
model_id = 'gtp-3.5-turbo'
openai.organization = 'org-S5OzuEyI144oLFwvCLpaot9R'


num_text = ()
results = []




def GPT3(query):
    responce = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": f"{query}"},
        ]
    )
    text3 = responce['choices'][0]['message']['content']
    print("************")
    return text3


def tag_wrap(text2):
    query = f"оберни текст в правильные html теги списка или параграфа: {text2}"
    responce = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": f"{query}"},
        ]
    )
    text5 = responce['choices'][0]['message']['content']
    time.sleep(1)
    return text5

def Chat_converstaion(text2, query_type,i, h2, img):

    # query_list = ['text_2_pr', 'text_1_pr', 'text_2_pr_7_spiski', 'h2_err', 'h2_advanatdes', 'text_main_think']
    # # weights = [3, 3, 3, 2, 2, 1]
    # query_type = random.choices(query_list, weights=(3,3,3,2,2,1), k=1)[0]


    # if query_type == 'text_del':
    #     query2 = f'Перепиши не меняя :"""{text2}"""'
    #     text4 = GPT3(query2)
    #     # num_text = (i, h2, text4,img)
    #     # results.append(num_text)
    #     # text6 = GPT3(text4)




    if query_type == 'text_2_pr':
        query = f'Я ученый, который пишет статью. Выдели 3-5 ключевых идей из текста. Добавь новые уточняющие мысли и факты:"""{text2}"""'
        text1 = GPT3(query)
        query2 = f'Я ученый пишущий статью. Напиши в виде простых абзацев. Раскрой пункты более связанно с дополнениями:"""{text1}"""'
        text4 = GPT3(query2)
        # text6 = GPT3(text4)
        print('Исполнение Нейронки', text4)



    if query_type == 'text_1_pr':
        query = f'Я ученый, который пишет статью. Выдели 3-5 ключевых идей из текста. Добавь новые уточняющие мысли и факты:"""{text2}"""'
        text1 = GPT3(query)
        query2 = f'Я ученый пишущий статью. Напиши в виде простых абзацев. Раскрой пункты более связанно с дополнениями:"""{text1}"""'
        text4 = GPT3(query2)
        # text6 = GPT3(text4)
        print(text4)

    elif query_type == 'h2_advanatdes':
        query_advantagess = f"Я ученый. Напиши на каждый способ преимущества и недостатки на текст: {text2}"
        text4 = GPT3(query_advantagess)
        print(text4)

    elif query_type == 'h2_err':
        query_h2 = f"Я ученый. Какие могут быть ошибки и их решения: {text2}"
        text4 = GPT3(query_h2)
        print(text4)

    elif query_type == 'text_2_pr_7_spiski':
        query = f'Я ученый, который пишет статью. Выдели 7-9 ключевых идей из текста. Добавь новые релевантные мысли и факты:"""{text2}'
        text1 = GPT3(query)
        query2 = f'Я ученый. Раскрой пункты более связанно с дополнениями.Напиши в виде списка. """{text1}"""'
        text4 = GPT3(query2)
        print(text4)

    elif query_type == 'text_main_think':
        query_quote = f"Я рецензент, который дает отзыв. Выдели одну ключевую практическую мысль с цифрами и фактами{text2}"
        text4 = GPT3(query_quote)
        print(text4)
        # print('<blockquote>',text4,'</blockquote>')


    elif query_type == 'text_main_think + eslino':
        query_quote = f"Я рецензент, который дает отзыв. Выдели одну ключевую практическую мысль с цифрами и фактами{text2}"
        text4 = GPT3(query_quote)
        print(text4)
        # print('<blockquote>',text4,'</blockquote>')
        query_rel = f"Какие последствия могут быть если не делать того что находится в тексте: {text4}"
        text5 = GPT3(query_rel)
        print(text5)

    elif query_type == 'text_table_advant_disadvant':
        # query = f"Я рецензент. Выдели в виде двух слов подлежащее и сказуемое{text2}"
        query = f"Сделай таблицу в тегах на 3 колонки(описание, преимущества, недостатки) из текста: {text2}"
        text3 = GPT3(query)
        print(text3)
        # query_2 = f"Чем можно заменить:{text3}"
        # text4 = GPT3(query_2)
        # print(text4)

    elif query_type == 'text_analog':
        pass
        # query = f"Я рецензент. Выдели в виде двух слов подлежащее и сказуемое{text2}"
        # text3 = GPT3(query)
        # query_2 = f"Чем можно заменить:{text3}"
        # text4 = GPT3(query_2)
        # print(text4)

    elif query_type == 'text_time_spent':
        # нормально если есть этапы (-)
        query = f"Выдели 5 этапов из текста: {text2}"
        text2 = GPT3(query)
        query2 = f"Сделай таблицу в тегах на 2 колонки (описание этапа, времязатраты в часах) из текста: {text2}"
        text4 = GPT3(query2)
        print(text4)

    elif query_type == 'h2_to_question':
        # нормально если есть этапы (-)
        query = f"Перефразируй в виде вопроса, если это вопрос то измени его с дополнением : {text2}"
        text4 = GPT3(query)
        print(text4)

    elif query_type == 'tag_wrap':
        query = f"оберни текст в правильные html теги списка или параграфа: {text2}"
        text4 = GPT3(query)
        print(text4)

    # новый текст с тегами
    # text4_in_tag = wrap_tags(text4)
    # делаем кортеж с тегами и отправляем в
    # num_text = (i, '<h2>' +h2+'</h2>', text4_in_tag, img)
    num_text = (i, h2, text4, img)

    results.append(num_text)
    return text4

    # query = f'Перепиши как агроном текст в тройных кавычках, повторять текст нельзя, возьми мысли из второго текста в тройных звездочках : """{text1}""", второй текст *** {text2}***'
    # query = f'распиши каждую из этих причин более подробно'
    # query = f'Напиши содержание статьи на тему: "Сорта гортензии метельчатой, самые красивые и устойчивые для посадки в саду"'
    # Конечно, вот статья на тему "Как подготовить гортензии к зиме" с обширными разделами и подразделами, которая составляет около 10 000 слов:
    # query = f'Напиши статью на 10000 символов по содержанию в тройных кавычках: """{text1}"""'
    # query = f'Сделай таблицу как ухаживать за гортензией зимой'
    # query =  f'Перефразируй текст, дополняя новые факты: """{text1}"""'

    # query = f'Выдели в виде списка 5 различных идей из текста:"""{text2}"""'
    # query3 = f'Сделай из текста html таблицу в 3 столбца: """{text3}"""'






    # query3 = f'Перепиши с новыми релевантными мыслями текст:"""{text2}"""'
    # responce3 = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo-16k-0613",
    #     messages=[
    #         {"role": "system", "content": ""},
    #         {"role": "user", "content": f"{query3}"},
    #     ]
    # )
    #
    # print(responce3['choices'][0]['message']['content'])
    #



# ----------------------------

# text = """"
# Размножение корневыми черенками
# """
text = """"
Сорта лука рекомендованные для весенней посадки
- Лук Центурион F1
- Лук Штутгартер Ризен
- Лук Ред Барон
- Лук Стурон
- Лук Геркулес
- Лук Стардаст
"""

#
# query_type = 'text_2_pr_7_spiski'
# # #
# raw_text = Chat_converstaion(text, query_type)
# print(raw_text)
# # ready_text = Chat_converstaion(raw_text, 'tag_wrap')
# # print(ready_text)