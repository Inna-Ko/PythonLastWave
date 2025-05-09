# Task 1

numbers = [3, 15, 17, 20, 48]
print(numbers[2])  # Выведите третий элемент списка `numbers`
numbers.append(10)  # Добавьте число 10 в конец списка `numbers`
numbers.remove(numbers[1])  # Удалите второй элемент из списка `numbers`
print(numbers)

# Task 2

fruits = ["mango", "dragonfruit", "banana"]
combined = numbers + fruits  # Объедините списки `numbers` и `fruits` в один новый список `combined`
combined_len = len(combined)  # Проверьте, сколько элементов находится в списке `combined`
print(combined[-1])  # Выведите последний элемент списка `combined`
combined_slice = combined[1:4]  # Создайте срез списка `combined`, который включает в себя элементы со второго по четвертый (включительно)

# Task 3

combined_copy = combined[3:6]  # Создайте копию списка `combined` с помощью среза
combined_copy[0] = "apple"  # Поменяйте значение первого элемента списка `combined_copy` на "яблоко"
print(combined)
print(combined_copy)
