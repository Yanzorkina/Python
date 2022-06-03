#8_1 подсчитать количество уникальных подстрок в строке
from hashlib import sha1

def count_unique(s):
    sub_set = set()
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            hash_el = sha1(s[i:j].encode('utf-8')).hexdigest()
            sub_set.add(hash_el)
    sub_set.discard(sha1(s[i:j].encode('utf-8')).hexdigest())
    sub_set.discard(sha1(s[i:j].encode('utf-8')).hexdigest())
    return len(sub_set)