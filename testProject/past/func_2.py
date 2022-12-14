'''
1. Запишите этот пример в файл скрипта и протестируйте его.
2. Измените код функции do_twice() так, чтобы она принимала два
аргумента, объект функции и значение и дважды вызывала функцию,
передавая значение в качестве аргумента.
3. Запишите определение функции print_twice(), приведенное ранее
в этой главе, в свой скрипт.
4. Используйте модифицированную версию функции do_twice(), чтобы
дважды вызвать функцию print_twice(), передав в качестве аргумента
значение 'спам'.
5. Определите новую функцию do_four(), которая принимает объект
функции и значение и вызывает функцию четыре раза, передавая
значение в качестве параметра. В теле этой функции должно быть
только две инструкции, а не четыре.
Решение: thinkpython2.com/code/do_four.py.
'''

def do_four(func, value):
    do_twice(func, value)
    do_twice(func, value)

def do_twice (func, value):
    func(value)
    func(value)

def print_spam(value):
    print(value)

do_four(print_spam, 'spam')
