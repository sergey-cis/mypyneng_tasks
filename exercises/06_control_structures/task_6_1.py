# -*- coding: utf-8 -*-
"""
Завдання 6.1

Список mac містить MAC-адреси у форматі XXXX:XXXX:XXXX однак, у обладнанні
Cisco MAC-адреси використовуються у форматі XXXX.XXXX.XXXX

Написати код, який перетворює MAC-адреси у формат cisco і додає їх у новий
список result (тест перевірятиме змінну result). Отриманий список результату
вивести на стандартний потік виведення (stdout) за допомогою print.

Приклад роботи завдання:
$ python task_6_1.py
['aabb.cc80.7000', 'aabb.dd80.7340', 'aabb.ee80.7000', 'aabb.ff80.7000']

Список mac не можна змінювати вручну, всі зміни треба робити за допомогою Python
"""

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

result = []

for maddr in mac:
    result.append(maddr.replace(":", "."))

print(result)
