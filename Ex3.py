# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

n = [8, 5, 3, 6, 0, 3, -1, 2, 2, 8, 1, 4, -1, 0]
new = []
for i in n:
    if i not in new:
        new.append(i)
print("Список: \n", n)
print("Список неповторяющихся чисел: \n", new)