# Task 1

def summ_a_b(a, b):
    summ = a + b
    return summ


def max_value(my_list):
    max_item = my_list[0]
    for my_list_item in my_list:
        if my_list_item > max_item:
            max_item = my_list_item
    return max_item


def greeting():
    name = input("Введите имя: ")
    print(f"Привет, {name}!")


# Task 2

def buy_ticket(full_name=None, age=None, adult=False):
    age = input("Введите возраст: ")
    if int(age) >= 18:    # тут еще нужна проверка, что введено числовое значение
        print("Билет продан")
    else:
        while not adult:
            adult_answer = input("Вас сопровождает взрослый? да/нет:  ")
            if adult_answer == "да":
                adult = True
                print("Билет продан под присмотром взрослого")
            elif adult_answer == "нет":
                print("Нельзя продать билет")
                break
            else:
                print("Ответ должен быть 'да' или 'нет'")


# Task 3

def square_of_numbers(*args):
    list_of_squares = []
    for arg in args:
        square_of_arg = arg*arg   # без доп проверок типа данных
        list_of_squares.append(square_of_arg)
    print(list_of_squares)
    return square_of_numbers

