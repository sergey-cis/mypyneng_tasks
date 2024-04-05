# -*- coding: utf-8 -*-
"""
Завдання 5.5a

Доповнити скрипт із завдання 5.5 таким чином, щоб, залежно від вибраного
режиму, задавалися різні запитання у запиті про номер VLAN або список VLANів:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter the allowed VLANs:'

Плюсом буде вирішити завдання без використання умови if та циклу for, але
перший варіант рішення краще зробити так, як виходитиме.
"""

access_template ="""
interface {}
switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""
from pprint import pprint
trunk_template ="""
interface {}
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan {}
"""
ask_mode_int = input("Enter interface mode (access/trunk): ").replace(" ", "").strip()
ask_num_int = input("Enter interface type and number: ").replace(" ", "").strip()



if ask_mode_int == "trunk":
    ask_vlan = input('Enter the allowed VLANs: ')
    print(trunk_template.format(ask_num_int,ask_vlan))
else:
    ask_vlan = input('Enter VLAN number: ')
    print(access_template.format(ask_num_int,ask_vlan))