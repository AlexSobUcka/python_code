import string



def has_no_e(word):
    if 'e' in word:
        return False
    return True


# True if string isn't in word
def avoids(word, string):
    for i in string:
        if i in word:
            return False
    return True


# string = input()


def sign_frequency(sign):
    fin = open('C:/Users/User/Downloads/words.txt')
    word_counter = 0
    no_sign_word_counter = 0
    for line in fin:
        word = line.strip()
        word_counter += 1
        if avoids(word, sign):
            no_sign_word_counter += 1
    return(no_sign_word_counter / word_counter * 100)


signs = list(string.ascii_lowercase)
least_uses = []

for i in signs:
    least_uses.append(sign_frequency(i))

least_uses.sort()
print(least_uses)