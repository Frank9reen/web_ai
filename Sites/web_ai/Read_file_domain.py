# Открывается файл с доменами и отправляется асинхронной функцией
import threading, os
from Parsing_all_page import parse_sitemap
th = []
with open("domains.txt") as domains:
    for domain in domains:
        thread = threading.Thread(target=parse_sitemap, args=(domain,))
        th.append(thread)
        thread.start()

    for t in th:
        t.join()
