#Напишите программу, доказывающую или проверяющую,
#что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число

import sys
import platform

n = int(input("введи данные n: "))
a = 0
for i in range(1,n+1):
    a += i
m = n * (n + 1) // 2
#print(a)
#print(m)


def show_sizeof(x, level=0):
    print ('\t' * level, x.__class__, sys.getsizeof(x), x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        else:
            for xx in x:
                show_sizeof(xx, level + 1)

#print(sys.getsizeof(n))
print(f'Общий объём памяти = {sys.getsizeof(a)} байт')
print(f'Общий объём памяти = {sys.getsizeof(n)} байт')
print(f'Общий объём памяти = {sys.getsizeof(m)} байт')
print (sys.platform)
print (sys.version)
