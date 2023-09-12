# Создание доменного имени на основе запроса к GPT3
import openai


openai.api_key = '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'
model_id = 'gtp-3.5-turbo'
openai.organization = 'org-S5OzuEyI144oLFwvCLpaot9R'


r = 'https://api.reg.ru/api/regru2/nop?username=test&password=test'



def GPT3():
    source = 'supersadovnik.ru'
    query = f'Я покупаю домен. Придумай на английском доменное имя аналогичное: {source}'
    responce = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": f"{query}"},
        ]
    )
    text = responce['choices'][0]['message']['content']
    return text


# ---------------
# print(GPT3())