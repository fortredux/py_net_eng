# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'

mac_new = '1234:1234:1234'
mac = mac_new.split(':')
mac0 = bin(int(mac[0]))
mac1 = bin(int(mac[1]))
mac2 = bin(int(mac[2]))
mac_final = mac0+mac1+mac2
print(mac_final[2:])