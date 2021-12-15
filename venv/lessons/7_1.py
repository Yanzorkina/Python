import os

new_list = {'my_project': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}

for k, v in new_list.items():
    if not os.path.exists(k):
        for item in v:
            for key in item.keys():
                os.makedirs(os.path.join(k, key))


