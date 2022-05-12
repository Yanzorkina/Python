# 3_1
answer = {}

for i in range(2,10):
    result = []
    for n in range(2,100):
        if n % i == 0:
            result.append(n)
    answer.update({i:len(result)})
print(answer)