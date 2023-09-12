import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# зададим массив текстов
some_texts = [
    'текст номер один',
    'текст следующий под номером два',
    'третий набор слов',
    'что-то ещё для полноценного дата-сета',
    'пример текстового документа',
]
df = pd.DataFrame({'texts': some_texts})

# А к данному тексту будем искать наиболее похожий из заданного выше набора
find_nearest_to = "текст номер три"

# формирование весов tf-idf
tfidf = TfidfVectorizer()
mx_tf = tfidf.fit_transform(some_texts)
new_entry = tfidf.transform([find_nearest_to])

# расчет косинусного расстояния
cosine_similarities = linear_kernel(new_entry, mx_tf).flatten()

# запишем все попарные результаты сравнений
df['cos_similarities'] = cosine_similarities
# и отсортируем по убыванию (т.к. cos(0)=1)
df = df.sort_values(by=['cos_similarities'], ascending=[0])

# Выведем 3 самых близких результата
for index, row in df[0:3].iterrows():
    print(row['texts'], row['cos_similarities'])
# output:
# текст номер один 0.7891589913464455
# текст следующий под номером два 0.23490553492076713
# третий набор слов 0.0