import difflib
import spacy
from spacy.lang.ru import Russian
nlp = spacy.load("ru_core_news_lg")


def similarity_dif(s1, s2):
  normalized1 = s1.lower()
  normalized2 = s2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()


def agenta (all_headers):
    # НАКИДАЛИ ВСЕ В ОДНО И ПОТОМ ОЧИСТИЛИ
    # all_headers = list(chain(headers, s22, s11))
    print(all_headers)
    for h2 in all_headers:
        noh2 = [x for x in all_headers if x != h2]
        q1 = nlp(h2)
        for el in noh2:
            q2 = nlp(el)
            if q1.similarity(q2) > 0.7 or similarity_dif(h2, el) > 0.5:
                try:
                    all_headers.remove(h2)
                except:
                    pass
    # for el in all_headers:
        # print('***', el)

    # МИКСОВАНИЕ СОЗДАННОГО СОДЕРЖАНИЯ (1)
    # Идем постепенно по общему содержанию, если видим что, что-то имеет близкую связь то ставим после
    index = 0
    new_all__headers = []
    end = len(all_headers)
    while index < end:
        elem = all_headers[index]
        if elem not in new_all__headers:
            new_all__headers.append(elem)
        # print('****************** ', elem)
        noh2 = all_headers.copy()
        del noh2[index]
        # print('noh2 --->', noh2)
        q1 = nlp(elem)
        for ee in noh2:
            q2 = nlp(ee)
            if q1.similarity(q2) > 0.3:
                # print(elem, '-----', ee, '---- ', q1.similarity(q2))
                # print('2222', new_all__headers)
                if ee not in new_all__headers:
                    new_all__headers.append(ee)
                break


        index = index + 1
    print(new_all__headers)
    # print(len(new_all__headers))
    return new_all__headers


# h1 = 'Многолетние флоксы – размножение, посадка, уход, обрезка'
#
# s1 = "Краткая информация о растении, популярные виды"
# s2 = "Размножение флоксов – вегетативное, семенами"
# s3 = "Посадка, удобрение"
# s4 = "Обрезка летом и осенью"
# s5 = 'Болезни и вредители'
# s6 = 'Флоксы Друммонда'
# s7 = 'Флокс метельчатый'
# s8 = 'Посадка, удобрение'
# s9 = "Флокс канадский"
# s10 = "Флоксы в ландшафтном дизайне — фото"
# s11 = "Флоксы в  дизайне — фото"
# headers = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]
#
# s1_1 ='Как размножают флоксы:'
# s1_2 ='Для чего нужно размножать флоксы?'
# s1_3 ='Флоксы в ландшафтном дизайне на даче'
# s1_4 ='Размножение весенними ростовыми побегами'
# s1_5 ='Размножение стеблевыми черенками'
# s1_6 ='Размножение листовыми черенками'
# s1_7 ='Размножение корневыми черенками'
# s1_8 ='Размножение семенами'
# s11 = [s1_1, s1_2, s1_3, s1_4, s1_5, s1_6, s1_7, s1_8]
#
# s2_1 = 'Посадка и уход за флоксами'
# s2_2 = 'Ботаническое описание'
# s2_3 = 'Выращивание флоксов из семян'
# s2_4 = 'Однолетние флоксы – посадка и уход'
# s2_5 = 'Уход за однолетними флоксами'
# s2_6 = 'Болезни и их лечение'
# s2_7 = 'Вредители и борьба с ними'
# s2_8 = 'Многолетние флоксы – посадка и уход'
# s2_9 = 'Как ухаживать за многолетними флоксами'
# s2_10 = 'Флоксы после цветения'
# s2_11 = 'Разновидности и сорта '
# s2_12 = 'Флоксы многолетние '
# s22 = [s2_1, s2_2, s2_3, s2_4, s2_5, s2_6, s2_7, s2_8, s2_9, s2_10, s2_11, s2_12]

#  ------------------- на ввод идет несколько списков Н2 --------
# all_headers = headers + s11 + s22
# agenta(all_headers)
# #
# #
#
#








# # Пример работы

# s1 = "Посадка, удобрение"
# s1_1 ='Посадка и уход за флоксами'
# q1 = nlp(s1)
# q2 = nlp(s1_1)
# # print(q1.similarity(q2))




# res = "\n".join("{}  -----  {}".format(x, y) for x, y in zip(all_headers, new_all__headers))
# print(res)
