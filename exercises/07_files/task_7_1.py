# -*- coding: utf-8 -*-
"""
Завдання 7.1

Обробити рядки з файлу ospf.txt і вивести інформацію щодо кожного рядка в
такому вигляді на стандартний потік виводу:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

"""
template = """Prefix              {:<20}
AD/Metric           {:<20}
Next-Hop            {:<20}
Last update         {:<20}
Outbound Interface  {:<20}
"""
from pprint import pprint
with open('ospf.txt', "r") as f:
    for l in f:
        splited = l.strip().split()
        pref, metric, n_hop, updt, out_intf = splited[1],splited[2],splited[4], splited[5],splited[6]
        print(template.format(pref.rstrip(), metric.rstrip().strip("[]"), n_hop.rstrip(","), updt.rstrip(","), out_intf.rstrip(",")))

    

