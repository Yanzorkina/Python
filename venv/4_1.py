from random import random
import cProfile
from time import time
def frequent(len_list):
    main_list = []
    count = {}
    for i in range(len_list):
        main_list.append(int(random()*10))
    #print(f'Список сгенерирован: {main_list}')
    for n in range(len(main_list)):
        if count.get(main_list[n]) == None:
            count.update({main_list[n]:1})
        else:
            count[main_list[n]] += 1
    #print(count)
    #print(f'Чаще остальных повторяется число : {max(count, key=count.get)}')
cProfile.run('frequent(10)')
cProfile.run('frequent(100)')
cProfile.run('frequent(1000)')
cProfile.run('frequent(10000)')
print('Видно, что количество операций нарастает линейно, строго пропорционально объему входных данных')
print('Посмотрим на время выполнения')
start = time()
frequent(10)
end = time()
finish = end - start
print(finish)
start = time()
frequent(100)
end = time()
finish = end - start
print(finish)
start = time()
frequent(1000)
end = time()
finish = end - start
print(finish)
start = time()
frequent(10000)
end = time()
finish = end - start
print(finish)
start = time()
frequent(100000)
end = time()
finish = end - start
print(finish)
start = time()
frequent(1000000)
end = time()
finish = end - start
print(finish)
start = time()
frequent(10000000)
end = time()
finish = end - start
print(finish)
print("Затраты времени показывают, что затраченное время так же линейно возрастает")