#Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры

import sys
import platform


a = int(input("введите данные a: "))
b = 1
d = 0
for i in range(a):
    d += b
    b /= -2
#print(d)

size = 0
list_size = 0
i = 0

vars = [a, b, d]

for v in vars:
    if type(v) == int or type(v) == str:
        size += sys.getsizeof(v)
    elif type(v) == list:
        for i in range(0, len(v) - 1):
            list_size += sys.getsizeof(v[i])
            i += 1
        all_list_size = sys.getsizeof(v) + list_size
        size += all_list_size
    #else:
        #print('Какой-то ещё тип переменной, который мы не обрабатываем')

print(f'Общий объём памяти = {size} байт')
print('system   :', platform.system())
print('processor:', platform.processor())
print("The Python version is %s.%s.%s" % sys.version_info[:3])
