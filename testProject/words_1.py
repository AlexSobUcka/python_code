fin = open('C:/Users/User/Downloads/words.txt')


def has_no_e(word):
    if 'e' in word:
        return False
    return True


def avoids(word, string):
    for i in string:
        if i in word:
            return False
    return True


word_counter = 0
no_e_word_counter = 0
string = input()


for line in fin:
    word = line.strip()
    word_counter += 1
    if avoids(word, string):
        no_e_word_counter += 1
        print(word)



print(no_e_word_counter/word_counter*100)
