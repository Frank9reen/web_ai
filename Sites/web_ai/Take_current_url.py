
def take_url(domain):
    list_urls = []
    with open('urls/'+domain, 'r') as file:
        s = file.read().splitlines()
        # вывести список всех урлов по домену
        # print(s)
        # list_urls.append()
    return s
# take_url('migrantplanet.com')