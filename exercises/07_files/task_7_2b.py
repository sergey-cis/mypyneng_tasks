# -*- coding: utf-8 -*-
"""
Завдання 7.2b

Скопіювати код із завдання 7.2a та переробити його: замість виведення на стандартний потік виведення, скрипт повинен записати отримані рядки у файл.

Імена файлів потрібно передавати як аргументи скрипту:
1 аргумент ім'я конфігураційного файлу з якого читаються рядки
2 аргумент ім'я файлу, в який будуть записані рядки

Приклад роботи завдання:
$ python task_7_2b.py config_sw1.txt new_config.txt

При цьому повинні бути відфільтровані рядки зі словами, які містяться в списку
ignore та рядки, що починаються на '!'.
"""
from pprint import pprint

ignore = ["duplex", "alias", "configuration", "end", "service"]

with open("config_sw1.txt", "r") as src, open("config_sw1_new.txt", "w") as dst:
    for line in src:
        if not line.startswith("!") and not any(word in line for word in ignore):
            dst.write(line)
            
