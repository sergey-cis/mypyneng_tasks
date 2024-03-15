# -*- coding: utf-8 -*-
"""
Завдання 5.4b

Все, як у завданні 5.4a, але, якщо користувач ввів адресу хоста, а не адресу
мережі, треба перетворити адресу хоста на адресу мережі та вивести адресу
мережі та маску, як у завданні 5.4a.

Приклад адреси мережі (усі біти хостової частини дорівнюють нулю):
* 10.0.1.0 255.255.255.0
* 190.1.0.0 255.255.0.0

Приклад адреси хоста:
* 10.0.1.1 255.255.255.0 - хост із мережі 10.0.1.0 255.255.255.0
* 10.0.5.195 255.255.255.240 - хост із мережі 10.0.5.192 255.255.255.240

Приклад роботи завдання якщо користувач ввів адресу 10.0.1.1 255.255.255.0,

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Перевірити роботу скрипту на різних комбінаціях хост/маска, наприклад:
    10.0.5.195 255.255.255.240, 10.0.1.1 255.255.255.0

Вивід має бути впорядкований як у прикладі:
* стовпцями
* ширина стовпця 10 символів (у двійковому форматі треба додати два пробіли між
  стовпцями для поділу октетів між собою)

Підказка: наприклад є адреса хоста у двійковому форматі та маска мережі 28.
Адреса мережі це перші 28 біт адреси хоста + 4 нуля. Тобто, наприклад, адреса
хоста 10.1.1.195/28 у двійковому форматі буде
bin_ip = "0000101000000001000000111000011"

А адреса мережі буде перших 28 символів з bin_ip + 0000 (4 тому що всього в
адресі може бути 32 біти, а 32 - 28 = 4)
00001010000000010000000111000000
"""
#My solution
#user_ip = input('Enter the IP and NetMask: ')
#input_list = user_ip.split(" ")
#
#ip_oct1, ip_oct2, ip_oct3, ip_oct4 = input_list[0].split(".")[0], input_list[0].split(".")[1], input_list[0].split(".")[2], input_list[0].split(".")[3]
#ip_bin = list("{:0>8b}".format(int(ip_oct1))+"{:0>8b}".format(int(ip_oct2))+ "{:0>8b}".format(int(ip_oct3))+ "{:0>8b}".format(int(ip_oct4)))
#
#
#
#m_oct1, m_oct2, m_oct3, m_oct4 = input_list[-1].split(".")[0], input_list[-1].split(".")[1],input_list[-1].split(".")[2],input_list[-1].split(".")[3]
#
#m_ripe = len((bin(int(m_oct1)) + bin((int(m_oct2))) + bin(int(m_oct3)) + bin(int(m_oct4))).replace("0b", "").replace("0", ""))
#ip_net = ("").join(ip_bin[:m_ripe]) + (32-m_ripe)*"0"
#ip_net_oct1, ip_net_oct2,ip_net_oct3,ip_net_oct4 = int(("").join(list(ip_net)[0:8]),2), int(("").join(list(ip_net)[8:16]),2), int(("").join(list(ip_net)[16:24]),2), int(("").join(list(ip_net)[24::]),2)
#
#template = """
#Network:
#{:<8}  {:<8}  {:<8}  {:<8}
#{:0>8b}  {:0>8b}  {:0>8b}  {:0>8b}
#Mask:
#/{}
#{:0>8b}  {:0>8b}  {:0>8b}  {:0>8b}
#"""
#print(template.format(ip_net_oct1, ip_net_oct2, ip_net_oct3, ip_net_oct4, int(ip_net_oct1), int(ip_net_oct2), int(ip_net_oct3), int(ip_net_oct4), m_ripe, int(m_oct1), int(m_oct2), int(m_oct3), int(m_oct4)))
#
user_ip = input('Enter the Network in forman(x.x.x.x x.x.x.x): ')
input_list = user_ip.split(" ")
# 
ip_list = input_list[0].split(".")
m_list = input_list[-1].split(".")

ip_oct1, ip_oct2, ip_oct3, ip_oct4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3])    
]

m_oct0, m_oct1,m_oct2,m_oct3 = [
    int(m_list[0]),
    int(m_list[1]),
    int(m_list[2]),
    int(m_list[3]),    
]

m_ripe = len((bin(m_oct0) + bin(m_oct1) + bin(m_oct2) + bin(m_oct3)).replace("0b", "").replace("0", ""))
ip_bin = ((bin(ip_oct1) + bin(ip_oct2) + bin(ip_oct3) + bin(ip_oct4)).replace("0b", "").replace("0", ""))
print(bin(ip_oct1).count("1"), bin(ip_oct1), "binary")
print(ip_bin) 
#ip_net = ("").join(ip_bin[:m_ripe]) + (32-m_ripe)*"0"

template = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:0>8b}  {1:0>8b}  {2:0>8b}  {3:0>8b}
Mask:
/{4}
{5:<8}  {6:<8}  {7:<8}  {8:<8}
{5:0>8b}  {6:0>8b}  {7:0>8b}  {8:0>8b}
"""
#print(template.format(ip_oct1, ip_oct2, ip_oct3, ip_oct4,  m_ripe, m_oct0, m_oct1, m_oct2, m_oct3))