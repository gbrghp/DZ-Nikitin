

#задача 1



arr = [[1, 2, 3], [5, 4, 3], [6, 7, 8]]
arr1 = []
arr2 = []
for i in range(3):
    arr1.append(arr[i][2])
for i in range(3):
    arr2.append(arr[1][i])
print(max(arr1), " ", max(arr2))



#задача 2

n = int(input("введите количество столбцов: "))
m = int(input("введите количество строк: "))
arr = list()
print("ввидите эллементы массива после ввода каждого эллемента нажмите enter")
for i in range(m):
    brr = list()
    for i in range(n):
        brr.append(int(input()))
    arr.append(brr)
for i in arr:
    print(' '.join(list(map(str, i))))
for i in range(m):
    for j in range(n):
        if arr[i][j] > 0:
            arr[i][j] = [1]
        else:
            arr[i][j] = [0]
for i in arr:
    print(' '.join(list(map(str, i))))

# задача 3

n = int(input("введите размер массива: "))
arr = list()
print("ввидите эллементы массива после ввода каждого эллемента нажмите enter")
for i in range(n):
    brr = list()
    for i in range(n):
        brr.append(int(input()))
    arr.append(brr)
arr1 = []
arr2 = []
c = 0
for i in range(n):
    c = 0
    arr1.append(sum(arr[i]))
    for j in range(n):
        c += arr[j][i]
    arr2.append(c)
if (arr1[0] / arr1[0]) * len(arr1) == len(arr1) and (arr2[0] / arr2[0]) * len(arr2) == len(arr2):
    print("матрица магическая")
else:
    print("матрица не магическая")

# задача 4

arr1 = []
n = int(input("введите размер массива: "))
arr = list()
print("ввидите эллементы массива после ввода каждого эллемента нажмите enter")
for i in range(n):
    brr = list()
    for i in range(n):
        brr.append(int(input()))
    arr.append(brr)
for i in range(n):
    for j in range(n):
        if i != j:
            if arr[i][j] == arr[j][i]:
                arr1.append(1)
            else:
                arr1.append(0)
if sum(arr1) == len(arr1):
    print("матрица симметричная")

# задача 5

n = int(input("введите количество столбцов: "))
m = int(input("введите количество строк: "))
arr = list()
print("ввидите эллементы массива после ввода каждого эллемента нажмите enter")
arr1 = []
for i in range(m):
    brr = list()
    for i in range(n):
        brr.append(int(input()))
    arr.append(brr)
for i in range(m):
    arr1.append(sum(arr[i]))
mx = arr1.index(max(arr1))
mn = arr1.index(min(arr1))
print("строка с наибольшей суммой эллементов: ", arr[mx], " ", max(arr1))
print("строка с наименьшей суммой эллементов: ", arr[mn], " ", min(arr1))

# задача 6

n = int(input("введите количество столбцов: "))
m = int(input("введите количество строк: "))
arr = [] * n
print("ввидите эллементы массива после ввода каждого эллемента нажмите enter")
for i in range(m):
    brr = [] * m
    for i in range(n):
        brr.append(int(input()))
    arr.append(brr)
for i in arr:
    print(' '.join(list(map(str, i))))
arr1 = [row[:] for row in arr]
for row in arr1:
    mn = min(row)
    for i in range(len(row)):
        if row[i] == mn:
            row[i] = 0 if mn % 2 == 0 else 1
for row in arr1:
    print(row)