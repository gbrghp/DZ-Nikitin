# задача 1

import math

def rad(x,y):
    return math.atan(y/x)

x1, x2 = map(float, input("введите координаты точки X через запятую: ").split(','))
y1, y2 = map(float, input("введите координаты точки Y через запятую: ").split(','))
z1, z2 = map(float, input("введите координаты точки Z через запятую: ").split(','))
x = rad(x1,x2)
y = rad(y1,y2)
z = rad(z1,z2)
if x<=y and x<=z:
    print(x1,x2)
if y<=x and y<=z:
    print(y1,y2)
if z<=x and z<=y:
    print(z1,z2)



# задача 2

n = int(input('Введите число до которого будут выводиться числа полиндромы '))
arr = []


def pol(x):
    c = 2
    while c * c <= x and x % c != 0:
        c += 1
    return c * c > x


for i in range(1, n + 1):
    if pol(i) and bin(i)[2: : ] == bin(i)[2::][::-1]:
        arr.append(i)
print('Простые натуральные числа, двоичная запись которых является палиндромом: ', ', '.join(map(str, arr)))