# задача 1

def read_last(lines,file):
    if lines > 0:
        c = file.readlines()
        l = len(c)
        for i in range((l-lines)-1,len(c)):
            print(c[i])
    else:
        print("вы ввели отрицательное число")

lines1 = int(input("введите количество последних строк: "))
file1 = open(input("введите путь файла: "))
read_last(lines1,file1)


# задача 4
import os

def main(filename):
    with open(filename, "w") as file:
        while True:
            line = input("Введите строку (для сохранения введите пустую строку или введите символ '!'): ")
            if line == '' or '!' in line:
                break
            file.write(line + "\n")

    print(f"Файл {filename} сохранен в ", os.getcwd())

filename1 = input("Введите имя будущего файла: ")
filename1 = filename1 + ".txt"
main(filename1)

# задача 3
def longest_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    words = text.split()

    max_length = max(len(word) for word in words)

    longest_words = [word for word in words if len(word) == max_length]

    return longest_words


file_path = "article.txt"
result = longest_words(file_path)
print("Самое длинное слово(а):", ', '.join(result))
