# -*- coding: utf-8 -*-
"""
Завдання 7.3b

Створити копію скрипта завдання 7.3a.

Переробити скрипт:
* запросити користувача ввести номер VLAN
* виводити інформацію лише за вказаним VLAN

Приклад роботи скрипта:
$ python task_7_3b.py
Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

"""
from pprint import pprint

asked_vlan = int(input("Enter VLAN number: "))
result = []
with open("CAM_table.txt", "r") as file:
    for line in file:
        columns = line.split()
        if len(columns) > 3 and columns[0][0].isdigit():
            vlan, mac, intf = columns[0].strip(), columns[1].strip(), columns[-1].strip()
            result.append([int(vlan),mac,intf])

sorted_result = sorted(result)
for vlan, mac, intf in sorted_result:
    if vlan == asked_vlan:
        print(f"{vlan:<10}{mac:20}{intf:20}")