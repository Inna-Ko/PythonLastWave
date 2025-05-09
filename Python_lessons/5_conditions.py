# Task 1

num = input("Введите число: ")

if int(num) == 0:
    print("Число равно нулю")
elif int(num) < 0:
    print("Число отрицательное")
elif 0 < int(num) < 10:
    print("Число от 1 до 9")
else:
    print("Число 10 или больше")

# Task 2

is_raining = True
is_sunny = False

if is_raining and is_sunny:
    print("Грибной дождик")
elif is_sunny and not is_raining:
    print("Пора прогуляться!")
elif is_raining and not is_sunny:
    print("Не забыть взят зонт")
else:
    print("Облачно, но без осадков")
