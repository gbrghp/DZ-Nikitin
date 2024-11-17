#задача 1
import math
R = int(input('R: \n'))
print(round(2*math.pi*R, 2))
print(round(math.pi*(R**2), 2))


# задача 3
import math
g = 9.81
L = int(input('Введите L:'))
T = 2*math.pi*math.sqrt(L/g)
print (round(T, 2))

# задача 2
x = 10
y = 55
print(x, y)
print(y, x)