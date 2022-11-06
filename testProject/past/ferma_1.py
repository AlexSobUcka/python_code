
def check_fermat(a, b, c, n):
    if a**n + b**n == c**n and n > 2:
        print('Не может быть, Ферма ошибся!')
    else:
        print('Нет, это не работает')

a = int(input('Введите число а:\n'))
b = int(input('Введите число b:\n'))
c = int(input('Введите число c:\n'))
n = int(input('Введите число n:\n'))

check_fermat(a, b, c, n)
