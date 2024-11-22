#задача 1
str = input()
str2 = ''
for i in range(len(str)):
   if str[i] == "н":
       str2 += str[i]
   else:
       str2 += " "
str_list2 = str2.split()
max = 0
for elem in str_list2:
    if len(elem) > max:
        max = len(elem)
        max_str = elem
index = str.find(max_str)
str = str[:index] + '!'* max + str[index + max:]
print(str)
print(f"Самая длинная последовательность н = {max}")

#задача 2
str = input()
str = str[str.find("(")+1:str.find(")")]
print(str)

#задача 3
str = input().split()
for i in str:
    i = i.lower()
    if i[0] == "a" and i[-1] == "я":
        print(i, end = ' ')