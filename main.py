import random

w = random.randint(4, 8)
h = random.randint(4, 8)

spisok = [-15, -4, -2, -7, 0, 3, 5, 12, 9]

matrix = []
index = 0
for i in range(w):
    list = []
    for j in range(h):
        list.append(spisok[index % len(spisok)])
        index += 1
    matrix.append(list)

for list in matrix:
    for num in list:
        print(f"|{num:{3}}", end="|")
    print()

sum = 0
for list in matrix:
    for num in list:
        if num % 3 != 0:
            sum += num

print(f"суммка не кратных 3: {sum}")
