import os

import django

root_dir = django.__path__[0]
django_files = {}

for root, dirs, files in os.walk(root_dir):
    for file in files:
        size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
        if django_files.get(size) == None:
            django_files[size] = 1
        else:
            django_files[size] += 1

for size, nums in sorted(django_files.items()):
    print(f'{size}: {nums}')



