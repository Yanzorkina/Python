nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный",
              "мягкий"]

from random import sample
from random import choices


def get_jokes(n, repeat=False):
    """Составит загадки из 3-х слов, взятых с каждого списка"""
    result = []

    if repeat == True:
        for nou, adv, adj in zip(choices(nouns, k=n), choices(adverbs, k=n), choices(adjectives, k=n)):
            result += [f'{nou} {adv} {adj}']
    else:
        for nou, adv, adj in zip(sample(nouns, n), sample(adverbs, n), sample(adjectives, n)):
            result += [f'{nou} {adv} {adj}']
    return result


print(get_jokes(5, repeat=True))