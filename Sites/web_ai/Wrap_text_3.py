import textile

text = """
1. вода
2. огонь
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

html = textile.textile(text)
print(html)