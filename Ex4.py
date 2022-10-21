# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#  Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
m = 100
k = int(input('Введите натуральную степень k:'))

koeff = [randint(0, m) for i in range(k)] + [randint(1, m)]
form = '+'.join([f'{(j,"")[j == 1]}x^{i}' 
for i, j in enumerate(koeff) if j][::-1])
form = form.replace('x^1+', 'x+')
form = form.replace('x^0', '')
form += ('','1') [form[-1] == '+']
form = (form, form[:-2]) [form[-2:] == '^1']
print(form)

with open('file.txt', 'w') as data:
    data.write(form)