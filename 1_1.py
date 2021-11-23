duration = int(input('Введите количество секунд: '))
sec_ = duration % 60
min_ = (duration % 3600)//60
hour_ = (duration % 86400)//3600
day_ = duration // 86400

result = [day_, hour_, min_, sec_]
sign = ['дн', 'часов', 'минут', 'секунд']

for i in range(len(result)):
    if result[i] > 0:
        print(result[i], sign[i], end = ' ')
        i = i + 1







#print (day, 'дней', hour, 'часов', min, 'минут')

