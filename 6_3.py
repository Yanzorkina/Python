from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        new = zip_longest(users, hobby, fillvalue=None)

        with open('uh.txt', 'w', encoding='utf-8') as f:
            for line in new:
                f.write(f'{str(line[0]).strip()}: {str(line[1]).strip()}\n')




