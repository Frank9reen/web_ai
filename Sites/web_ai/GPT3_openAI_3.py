# Создание нового текста от вопроса в OPENAI

import openai
import os

openai.api_key = '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'
model_id = 'gtp-3.5-turbo'
openai.organization = 'org-S5OzuEyI144oLFwvCLpaot9R'


def Chat_converstaion():
    text22 = """"
     """


    text2 = """"
    Размножение корневыми черенками
    """



    # query = f'Перепиши как агроном текст в тройных кавычках, повторять текст нельзя, возьми мысли из второго текста в тройных звездочках : """{text1}""", второй текст *** {text2}***'
    # query = f'распиши каждую из этих причин более подробно'
    # query = f'Напиши содержание статьи на тему: "Сорта гортензии метельчатой, самые красивые и устойчивые для посадки в саду"'
    # Конечно, вот статья на тему "Как подготовить гортензии к зиме" с обширными разделами и подразделами, которая составляет около 10 000 слов:
    # query = f'Напиши статью на 10000 символов по содержанию в тройных кавычках: """{text1}"""'
    # query = f'Сделай таблицу как ухаживать за гортензией зимой'
    # query =  f'Перефразируй текст, дополняя новые факты: """{text1}"""'

    # query = f'Выдели в виде списка 5 различных идей из текста:"""{text2}"""'
    # query3 = f'Сделай из текста html таблицу в 3 столбца: """{text3}"""'


    # query = f'Я ученый, который пишет статью. Выдели 3-5 ключевых идей из текста. Добавь новые уточняющие мысли и факты:"""{text2}"""'
    # responce = openai.ChatCompletion.create(
    # model="gpt-3.5-turbo-16k-0613",
    # messages=[
    #         {"role": "system", "content": ""},
    #         {"role": "user", "content": f"{query}"},
    #     ]
    # )
    # text1 = responce['choices'][0]['message']['content']
    # # print(text1)

    # query3 = f'Сделай из текста html таблицу в 3 столбца: """{text1}"""'
    # query2 = f'Раскрой пункты более связанно с дополнениями и новыми фактами. Напиши в виде простых абзацев."""{text1}"""'
    # responce2 = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo-16k-0613",
    #     messages=[
    #         {"role": "system", "content": ""},
    #         {"role": "user", "content": f"{query2}"},
    #     ]
    # )
    # text2 = responce2['choices'][0]['message']['content']
    # # print(text2)

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
    # query_quote = f"Я рецензент, который дает отзыв. Выдели одну ключевую практическую мысль с цифрами и фактами{text2}"
    # responce3 = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo-16k-0613",
    #     messages=[
    #         {"role": "system", "content": ""},
    #         {"role": "user", "content": f"{query_quote}"},
    #     ]
    # )
    #
    # print('qote ---- ', responce3['choices'][0]['message']['content'])

    #
    # делается по подзаголовку!
    #
    query_table = f"Я ученый. Напиши на каждый способ преимущества и недостатки на текст: {text2}"
    responce3 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": f"{query_table}"},
        ]
    )

    print('table ---- ', responce3['choices'][0]['message']['content'])

    # ETXT 91
    # query_h2 = f"Я ученый. Какие могут быть ошибки и их решения: {text2}"
    # responce3 = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo-16k-0613",
    #     messages=[
    #         {"role": "system", "content": ""},
    #         {"role": "user", "content": f"{query_h2}"},
    #     ]
    # )
    #
    # print('table ---- ', responce3['choices'][0]['message']['content'])


def gpe3(stext):
    # openai.api_key = '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'


    list_model = openai.Model.list()
    # print(list_model)
    # query = 'Перефразируй то что находится в тройных кавычках расширяя новыми фактами: """Многие дачники, которые растение гортензии ориентируются на то, что гортензия должна цвести с появлением весны. Однако иногда возникают трудности, в результате которых растение может просто не цвести. Причины этого могут быть различными, начиная от неверной обрезки и повреждения бутонов, заканчивая ложным расположением и предоставлением слишком много удобрений. Чтобы обеспечить правильный цветение гортензии, необходимо уделить ему дополнительное внимание: проверить положение, придать гортензии правильную форму с помощью правильной обрезки, а также учитывать наличие удобрений."""'

    # response = openai.Completion.create(
    #     model="gpt-3.5-turbo-instruct",
    #     prompt=f"{query}",
    #     temperature=1,
    #     max_tokens=256,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0
    # )
    # print(response)
    # list_gpt = response.choices[0]
    #
    # list_gpt = response.choices[0].text.split('\n')

    #
    # if len(list_gpt) > 1:
    #     tt = list_gpt[-1]
    #     # print(list_gpt[-1])
    # else:
    #     tt = response.choices[0].text
    #
    # return tt



# print(gpe3(query))
Chat_converstaion()