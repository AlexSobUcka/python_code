'''
Напишите функцию right_justify(), которая принимает строку s в каче-
стве параметра и печатает строку с достаточным количеством пробелов
в начале строки, так чтобы последняя буква строки находилась в столбце 70
на экране:
'''

def right_justify(string):
    empty = ' '
    lenght = len(string)
    need_to_add = 70 - lenght
    print(need_to_add * empty + string)

right_justify('string')