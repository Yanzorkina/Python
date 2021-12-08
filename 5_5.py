
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


print([el for el in src if src.count(el) == 1])
#----------------------------------------------------------------
unique_num = set()
src_2 = set()
for n in src:
    if n not in src_2:
        unique_num.add(n)
    else:
        unique_num.discard(n)
    src_2.add(n)
print(unique_num)


unique_nums = [n for n in src if n in unique_num]
print(unique_nums)








