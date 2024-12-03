#задача 1
a = int(input())
total = 0
for i in range(1, a):
    total = total + i ** 3
print(total)

#задача 2
for i in range(1, 10):

    for j in range(1, 10):
        print(i, 'x', j, '=', i * j, end="  ")

    print()

