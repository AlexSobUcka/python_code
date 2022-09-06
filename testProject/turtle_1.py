import turtle
from math import pi
bob = turtle.Turtle()
length = 50

def square(t, length):
    polygon(t, length, 4)

def circle(t, r):
    arc(t, r, 360)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    print(t)
    turtle.mainloop()

def arc(t, r, angle):
    length = 2 * pi * r / 60
    n = int(angle / 6)
    for i in range(n):
        t.fd(length)
        t.lt(6)
    print(t)


def petal(t, r, angle):
    '''
    :param n: количество листов
    :param r: радиус листа
    '''
    for i in range(2):
        arc(bob, r, angle)
        t.lt(180 - angle)


def flower(t, n, r):
    '''
    :param t: черепаха
    :param n: количество листов
    :param r: длинна листа
    '''
    angle = 360 / n
    for i in range(n):
        petal(t, r, angle)
        t.lt(angle)


#square(bob, 50)
#circle(bob, 100)
#arc(bob, 50, 90)
#flower(bob, 10, 100)
#turtle.mainloop()
#polygon(bob, 200, 8)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

def Koch(t, length):
    if length < 10:
        t.fd(length)
        return
    n = length / 3
    Koch(t, n)
    t.lt(60)
    Koch(t, n)
    t.rt(120)
    Koch(t, n)
    t.lt(60)
    Koch(t, n)

def snowflake(t):
    for i in range(3):
        Koch(t, 2500)
        t.rt(120)

snowflake(bob)