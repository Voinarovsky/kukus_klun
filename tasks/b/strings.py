"""
Считайте с клавиатуры две строки.

Выведите по очереди:
- [a] произведение длин этих строк
- [b] обе эти строки, разделенные пробелом
- [c] обе эти строки, разделенные запятой и табуляцией
- [d] строку вида "Hello, {первая строка}! Just wanted to say: '{вторая строка}'"
    > подсказка: используйте форматную строку (f-string)
- [e] первые "слова" из каждой строки через пробел
    > под "словами" имеются в виду части строки, разделенные друг от друга пробелами
- [f] количество "слов" в первой строке
- [g] первую позицию вхождения первой строки во вторую (или -1, если их нет)
"""

s1 = input()
s2 = input()
print(len(s1)*len(s2))
print(s1,' ',s2)


# Место для вашего кода
