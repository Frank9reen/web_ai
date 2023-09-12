import re

text = """
1) вода
2) огонь
- медные трубы
Колыбельная метла

и что
- первы
- второй
-третий
как это понимать
1) re
2) de
3) fe
sdafasdf
asdf
"""
text2 = """
1.Выбор подходящих сортов лука для весенней посадки 
2.Сорт лука "Центурион F1" рекомендуется для весенней посадки 
3.Сорт "Штутгартер Ризен" рекомендуется для весенней посадки 
4.Сорт "Ред Барон" рекомендуется для весенней посадки 
5.Сорт "Стурон", "Геркулес" и "Стардаст" могут быть надежными вариантами для выращивания весеннего лука 
6.У каждого из этих сортов лука могут быть уникальные свойства, подходящие для весенней посадки 
7.Рекомендуется провести дополнительные исследования о каждом из этих сортов лука 
8.Нужно учитывать климатические особенности региона при выборе сорта лука для весенней посадки 
9.Оптимальное время для весенней посадки лука может различаться в зависимости от региона.
1.Выбор подходящих сортов лука для весенней посадки 
2.Сорт лука "Центурион F1" рекомендуется для весенней посадки 
3.Сорт "Штутгартер Ризен" рекомендуется для весенней посадки 
4.Сорт "Ред Барон" рекомендуется для весенней посадки 
5.Сорт "Стурон", "Геркулес" и "Стардаст" могут быть надежными вариантами для выращивания весеннего лука 
6.У каждого из этих сортов лука могут быть уникальные свойства, подходящие для весенней посадки 
7.Рекомендуется провести дополнительные исследования о каждом из этих сортов лука 
8.Нужно учитывать климатические особенности региона при выборе сорта лука для весенней посадки 
9.Оптимальное время для весенней посадки лука может различаться в зависимости от региона.

"""

def wrap_tags(text2):
    ls = text2.splitlines()
    print(ls)
    ls_new = []
    count = 0
    flag = False
    ferst_li = True

    # Пошли по строкам
    for l in ls:
        count += 1

        # Если строка пустая идем дальше
        if l == "":
            continue


        try:
            nums = re.search(r'\d\.|\d\)', l).group(0)
            print(nums)

            if ferst_li == True:
                str_li = '<ol><li>' + l.replace(nums, "") + '</li>'
                ls_new.append(str_li)
                ferst_li = False
                flag = True
            else:
                str_li = '<li>' + l.replace(nums, "") + '</li>'
                ls_new.append(str_li)
                flag = True

        # except:
            # # ищу еслить ли маркеры в начале статьи (-) этот блок можно убрать если оставить только цифры без маркеров
            # try:
            #     marks = re.search(r'\-', l).group(0)
            #     print(marks)
            #     str_li = '<li>' + l.replace(marks, "") + '</li>'
            #     ls_new.append(str_li)



        except:
            # Попадаю сюда если не находит цифр для создания завершенного выбора для цифр
            ferst_li = True
            if flag == True:
                str_p = '<p>' + l + '</p>'
                ls_new.append('</ol>' + str_p)
                flag = False
            else:
                str_p = '<p>' + l + '</p>'
                ls_new.append(str_p)
            continue
    print(ls_new)

    # Сбор строк в текст html
    for string in ls_new:
        print(string)

    return string
# wrap_tags(text)