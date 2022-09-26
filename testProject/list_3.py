fin = open('C:/Users/User/Downloads/words.txt')
word_list = []
for line in fin:
    word = line.strip()
    #word_list.append(word)
    word_list += [word]

print(word_list)