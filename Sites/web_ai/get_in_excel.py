import pandas as pd


def get_in_excel(h2_text_img_list: list):
    df = pd.DataFrame(h2_text_img_list)
    df[1] = df[1].str.replace('\n', '')
    df[1] = df[1].str.replace('\t', ' ')
    df[1] = df[1].str.replace(' {2,}', ' ', regex=True)
    df[1] = df[1].str.strip()

    writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()
    df = pd.read_excel('test.xlsx')
    df2 = df.dropna()  # удаление строк пустых

    df2.to_excel('test.xlsx', index=False)
    print(df2)
    return