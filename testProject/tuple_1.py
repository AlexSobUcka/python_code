import re


def histogram(s):
    """
        принимает строку и возвращает словарь частотности букв
    """
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def most_frequent(text):
    """
    принимает строку и печатает буквы в порядке убывания их частотности
    """
    reg = re.compile('[^a-zA-Z ]')
    text = reg.sub('', text)
    temp_dict = histogram(text)

    t = []
    for key, value in temp_dict.items():
        t.append((value, key))
    t.sort(reverse=True)

    for i in t:
        print(i[1])


def read_file(filename):
    """Returns the contents of a file as a string."""
    return open(filename).read()


text = read_file('C:/Users/spopo/Downloads/text.txt')
most_frequent(text)