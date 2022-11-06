#fin = open('C:/Users/User/Downloads/words.txt')
fin = open('C:/Users/Aleksandr/Downloads/words.txt')

"""
words = dict()
for line in fin:
    word = line.strip()
    words[word] = 0
"""


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


h = histogram('попугоивпылоиукрырк')
k = invert_dict(h)

inverse = dict()
for key in h:

    inverse.setdefault(h[key], []).append(key)
print(h)
print(inverse)


