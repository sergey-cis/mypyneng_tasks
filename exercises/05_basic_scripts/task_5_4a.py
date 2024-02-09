# -*- coding: utf-8 -*-
"""
Завдання 5.4a

Запросити користувача введення IP-мережі у форматі: 10.1.1.0 255.255.255.0

Потім вивести інформацію про мережу та маску в такому форматі:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Перевірити роботу скрипта на різних комбінаціях мережа/маска.

Вивід має бути впорядкований як у прикладі:
* стовпцями
* ширина стовпця 10 символів (у двійковому форматі треба додати два пробіли між
  стовпцями для поділу октетів між собою)

Приклад роботи завдання:

$ python task_5_4a.py
Enter network address: 10.1.1.0 255.255.255.0

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


$ python task_5_4a.py
Enter network address: 10.1.1.192 255.255.255.240

Network:
10        1         1         192
00001010  00000001  00000001  11000000

Mask:
/28
255       255       255       240
11111111  11111111  11111111  11110000
"""

user_ip = input('Enter the IP and NetMask: ')
input_list = user_ip.split(" ")
ip_oct1, ip_oct2, ip_oct3, ip_oct4 = input_list[0].split(".")[0], input_list[0].split(".")[1], input_list[0].split(".")[2], input_list[0].split(".")[3]
m_oct1, m_oct2, m_oct3, m_oct4 = input_list[-1].split(".")[0], input_list[-1].split(".")[1],input_list[-1].split(".")[2],input_list[-1].split(".")[3]

m_ripe = len((bin(int(m_oct1)) + bin((int(m_oct2))) + bin(int(m_oct3)) + bin(int(m_oct4))).replace("0b", "").replace("0", ""))



template = """
        Network:
          {:<8}  {:<8}  {:<8}  {:<8}
          {:0>8b}  {:0>8b}  {:0>8b}  {:0>8b}
        Mask:
         /{  }
          {:0>8b}  {:0>8b}  {:0>8b}  {:0>8b}
      """
print(template.format(ip_oct1, ip_oct2, ip_oct3, ip_oct4, int(ip_oct1), int(ip_oct2), int(ip_oct3), int(ip_oct4), m_ripe, int(m_oct1), int(m_oct2), int(m_oct3), int(m_oct4)))

