# -*- coding: utf-8 -*-
"""
Завдання 7.4

Створити скрипт, який оброблятиме конфігураційний файл комутатора і
отримуватиме з нього інформацію про порти в режимі trunk і вланах, які
налаштовані на цих портах.

Ім'я конфігураційного файлу передається як аргумент скрипту.
$ python task_7_4.py config_trunk_sw2.txt
$ python task_7_4.py config_trunk_sw3.txt

Передавати ім'я файлу як аргумент скрипту. Вказаний конфіг потрібно обробити і
отримати словник портів у режимі trunk, де ключі номери портів, а значення
список дозволених VLAN (список рядків).

Записати підсумковий словник у змінну trunk_dict (саме ця змінна
перевірятиметься у тесті). За бажанням можна виводити словник на екран, тест
перевіряє лише вміст змінної. Тут зручно виводити словник за допомогою pprint.

Наприклад, для файлу config_trunk_sw2.txt повинен вийти такий словник:
$ python task_7_4.py config_trunk_sw2.txt
{'FastEthernet0/1': ['100', '200'],
 'FastEthernet0/3': ['100', '300', '400', '500', '600'],
 'FastEthernet0/4': ['400', '500', '600']}

Для файлу config_trunk_sw3.txt повинен вийти такий словник:
$ python task_7_4.py config_trunk_sw3.txt
{'FastEthernet0/1': ['10', '20', '21', '22'],
 'FastEthernet0/2': ['10', '13', '1450', '1451', '1452'],
 'FastEthernet0/6': ['40', '50', '60']}

Перевірити роботу функції на прикладі файлів config_trunk_sw2.txt та
config_trunk_sw3.txt. Переконайтеся, що в результаі для цих файлів виходять
вірні словники.

Підказка щодо синтаксису cisco: у цьому завданні вважаємо, що інтерфейс
знаходиться в режимі trunk, якщо в нього налаштована команда:
switchport trunk allowed vlan.
"""
from pprint import pprint
#import sys
from sys import argv
#Send data by the sys.argv
try:
    file = argv[1]
except(NameError, IndexError):
    print("You have to enter file name")

#print(sys.argv) or print(argv)
trunk_dict = {}

try:
    with open(file, "r") as f:
        for line in f:
            if line.startswith("interface"):
                intf = line.split()[-1]
            elif line.startswith(" switchport trunk allowed"):
                trunk_dict[intf] = []
                trun = line.split()[-1].strip()
                trunk_dict[intf].append(trun)
except NameError:
    print("Give me please file")
pprint(trunk_dict)