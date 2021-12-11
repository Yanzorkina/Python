import sys

with open('bakery.csv', 'r', encoding='utf-8') as sale:
    if len(sys.argv) == 1:
        print(sale.read())
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        for i, v in enumerate(sale):
            if i + 2 > int(sys.argv[1]):
                print(v)
    if len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit() and sys.argv[1] < sys.argv[2]:
        for i, v in enumerate(sale):
            if i + 2 > int(sys.argv[1]) and i < int(sys.argv[2]):
                print(v)
