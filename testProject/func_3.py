'''
Напишите функцию, которая рисует сетку следующим образом:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
'''

def box(col_number, row_number):
    for i in range(row_number):
        box_row(col_number)
    print('+ - - - -' * col_number, '+')

def box_row(col_number):
    first_line = '+ - - - -'
    line = '|        '
    print(first_line * col_number, '+')
    print(line * col_number, '|')
    print(line * col_number, '|')
    print(line * col_number, '|')

box(1, 5)
