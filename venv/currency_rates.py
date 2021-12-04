
from requests import get, utils
from decimal import Decimal
from datetime import date


response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)




def currency_rates(valute):
    d, m, y = (content.split('<ValCurs Date="')[1][0:10]).split(".")
    date_1 = date(year=int(y), month=int(m), day=int(d))
    print(date_1)

    for i in content.split('<Valute ID='):
        if i.find(valute.upper()) != -1:
            #return float((i.split('Value>'))[1][0:-2].replace(",", "."))
            return Decimal((i.split('Value>'))[1][0:-2].replace(",", "."))


if __name__ == "__main__":
    print(currency_rates("uSD"))
    print(currency_rates("EUR"))

