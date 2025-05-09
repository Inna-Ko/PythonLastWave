# Task 1 - Среднее кол-во символов в словах строки

string = "Test100000 Test2 T100 T100 1"

split_string = string.split(" ")
summary_len = 0
split_string_len = len(split_string)

for word in split_string:
    word_len = len(word)
    summary_len = summary_len + word_len

average_len = summary_len / split_string_len

print(average_len)

# Task 2 - Пример декоратора

def my_decorator(func):
    def my_wrapper():
        print("Hi!")
        func()
        print("Bye")
    return my_wrapper

@my_decorator
def print_text():
    print("Blah-blah-blah")

print_text()


# Task 3 - Найти самое длинное слово в списке

my_list = ["hi", "intelligent", "world", "indigo"]

max_len = len(my_list[0])
max_len_word = my_list[0]

for word in my_list:
    if len(word) > max_len:
        max_len = len(word)
        max_len_word = word

print(max_len_word)


# Task 4 - Найти самый частый элемент в списке

my_list = [1, 2, 2, 3, 4, 7, 5, 6, 7, 7]


def most_common_element(my_list):
    if not my_list:
        return None  # Если список пустой, возвращаем None

    frequency_dict = {}  # Словарь для хранения частот элементов

    for element in my_list:

        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

    print(max(frequency_dict, key=frequency_dict.get))
    return max(frequency_dict)

most_common_element(my_list)


# Task 5 - Палиндром

my_string = "abcdedcb"
inverted_string = my_string[::-1]

if my_string == inverted_string:
    print("Палиндром")
else:
    print("Не палиндром")