import sys

with open('bakery.csv', 'a', encoding='utf-8') as sale:
    if sys.argv[1].replace(",", "").isdigit() == True:
        sale.write(f'{sys.argv[1]}\n')
    else:
        print('При вводе цены используйте цифры и запятую')
