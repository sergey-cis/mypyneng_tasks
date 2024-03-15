# -*- coding: utf-8 -*-
"""
Завдання 7.3

Скрипт повинен обробляти записи у файлі CAM_table.txt. Кожен рядок, де є
MAC-адреса, має бути оброблена таким чином, щоб на стандартний потік виведення
була виведена таблиця виду:

100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9

"""
from pprint import pprint

with open("CAM_table.txt", "r") as file:
    for line in file:
        columns = line.split()
        if len(columns) > 3 and columns[0][0].isdigit():
            vlan, mac, intf = columns[0].strip(), columns[1].strip(), columns[-1].strip()
            print(f"{vlan:<8} {mac:<15} {intf:>10}")