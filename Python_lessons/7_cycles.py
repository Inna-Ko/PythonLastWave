# Task 1

demo_list = []
for num in range(0, 101):
    demo_list.append(num)

# Task 2
while len(demo_list) > 51:
    demo_list.pop(-1)
print(demo_list)

# Task 3
num = 1
while num < 101:
    if num % 7 == 0:
        print(num)
        break
    else:
        num += 1
