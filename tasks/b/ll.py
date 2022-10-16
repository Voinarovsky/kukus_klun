"""
Вам дана переменная n, в которую записано целое число.

Создайте массив a длины n, в котором каждое следующее число так же
генерируется функцией get_integer().

Выведите по очереди:
- сам массив
    > уже написано за вас
- [a] первый, медианный (центральный) и последний элемент массива через пробел
- [b] минимальный и максимальный элементы массива через пробел
- [c] сумму всех элементов массива
- [d] массив, состоящий из квадратов всех четных элементов a
- [e] позицию первого вхождения минимального элемента в a
- [f] развернутый массив a
    > подсказка: используйте встроенную функцию или срез
- [g] массив, состоящий из всех элементов a на четных позициях
    > подсказка: используйте срез
"""

from test.common.context import get_integer

a = []
n = get_integer()
for i in range(0,n+1):
    b = get_integer()
    a.append(b)
print(a)
# Место для вашего кода (заполнение массива)

print(a)
print(n)
print(len(a))
print(a[0], a[n//2], a[n-1])


# Место для вашего кода
