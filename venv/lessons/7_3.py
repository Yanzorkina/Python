import os
import shutil

root_dir = "my_project"

for root, dirs, files in os.walk(root_dir):
    for file in files:

        app_dir = os.path.abspath(root).split("\\")[-3]
        if file.endswith('.html') and app_dir != root_dir:
            try:
                shutil.copytree(root, os.path.join('my_project', "templates", app_dir))

            except FileExistsError as e:
                print(f'В одной из папок несколько подходящих по условию файлов \n {e}')








