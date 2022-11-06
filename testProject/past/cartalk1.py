import string

fin = open('C:/Users/Aleksandr/Downloads/words.txt')
signs = list(string.ascii_lowercase)

word_counter = 0

#check if sign double
def is_double(index, word):
    if word[index + 1] == word[index]:
        return True
    return False

for line in fin:
    word = line.strip()
    index = 0
    for index in range(len(word)-5):
        if is_double(index, word):
            index += 2
            if is_double(index, word):
                index += 2
                if is_double(index, word):
                    print(word)
        index += 1



