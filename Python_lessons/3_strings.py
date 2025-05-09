# Task 1

test_string = "text"

print(test_string[0])
print(test_string[-1])
print(test_string[1:3])
print(len(test_string))

# Task 2

name = "Инна"
age = "37"
message = "Меня зовут " + name + " и мне " + age + " лет."
message_f = f"Меня зовут {name} и мне {age} лет."
text_to_escape_1 = r"~!@#$%^&*()_+-={}[]\|/`'"+"\""  # двойные кавычки в r-строку добавить не получилось, т.к. она задана в таких кавычках
text_to_escape_2 = "~!@#$%^&*()_+-={}[]\|/`\'\"\\"

# Task 3

text = "Python - лучший язык для автоматизации!"
contains_python = "Python" in text

text_2 = "Мы работаем, чтобы стать лучше"
text_2_replace = text_2.replace(" ", "*")

text_ends_with_symbol = text.endswith("!")
text_upper = text.upper()
text_lower = text.lower()



