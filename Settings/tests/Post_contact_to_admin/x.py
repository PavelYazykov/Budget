import random
"""открытие файла"""
# with open('../../methods/files/symbols_20.txt', 'r') as string:
#     x = string.read()
#     print(x)


def randstr(chars='qwertyu', n=10):
    return ''.join(random.choice(chars) for _ in range(n))


print(randstr(n=19000))
