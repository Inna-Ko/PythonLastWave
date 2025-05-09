# Task 1
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Task 2
name = input("Введите имя: ")
age = input("Введите возраст: ")

with open('userinfo.txt', 'a') as file:
    file.write(f"{name}: {age}\n")

# Task 3

with open('copy.txt', 'w') as file_copy:
    with open('original.txt', 'r') as file_original:
        for line in file_original:
            file_copy.write(line)
