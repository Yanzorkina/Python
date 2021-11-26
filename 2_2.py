message = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, v in enumerate(message):
    if v.isdigit():
        message[i] = f'"{int(v):02}"'
    elif v[1:].isdigit():
        message[i] = f'"{v[0]}{int(v[1:]):02}"'

print(message)
print(' '.join(message))