def write_domain(domain):
    with open('Block_domains.txt', 'a') as file:
        file.writelines(domain + '\n')