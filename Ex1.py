# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.    10^(-1) ≤ d ≤10^(-10)
import math
p = math.pi
x = int(input('Введите количество вычислений Лейбница: '))

for i in range(x+1):
    if (i == 0):
        a = 3
        b = 1
        pi = 4/b - 4/a
    if(i > 1):
        a += 4
        b += 4
        pi = pi + (4/b - 4/a)
print("Равно = ", pi)
print(f"Число П = ", p)
print(f"Точность = ", (100 * (pi - p) / -p))