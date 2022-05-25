
'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего.
'''
from collections import defaultdict
def input_info(n_fact): #Собирает у пользователя информацию и возвращает словарь
    factories_data = defaultdict(list)
    for i in range(n_fact):
        factories_data[i].append(
            [
            input(f'Введите название предприятия номер {i+1}: '),
            float(input('Введите прибыль\nЗа первый квартал: ')),
            float(input('За второй: ')),
            float(input('За третий: ')),
            float(input('За четвертый: '))
                ]
        )
    return factories_data
def get_middle(fctry_dict):  # Принимает словарь, возвращает среднюю годовую прибыль
    sum_all = 0
    len_all = 0
    for j in range(n_fact):
        sum_all += sum(factories_data[j][0][1:])
        len_all += 1
    middle = sum_all / len_all
    return middle
def print_good_n_bad(factories_data, middle):
    good_fact = []
    bad_fact = []
    for k in range(n_fact):
        if sum(factories_data[k][0][1:]) > middle:
            good_fact.append(factories_data[k][0][0])
        else:
            bad_fact.append(factories_data[k][0][0])
    print(f'Выше среднего: {good_fact}')
    print(f'Ниже среднего: {bad_fact}')
n_fact = int(input('Введите количество предприятий: '))
factories_data = input_info(n_fact)
#print(factories_data)
middle = get_middle(factories_data)
print(f'Средняя годовая прибыль: {middle}')
print_good_n_bad(factories_data, middle)