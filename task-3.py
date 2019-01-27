#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве
import sys
import platform
from random import random

N = 10
arr = []
for a in range(N):
        arr.append(int(random() * 200) - 70)
print(arr)
 
a = 0
index = -1
while a < N:
        if arr[a] < 0 and index == -1:
                index = a
        elif arr[a] < 0 and arr[a] > arr[index]:
                index = a
        a += 1

size = 0
list_size = 0
i = 0

vars = [a, N, i]

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
print('Номер элемента :' , index+1,'Максимальное отрицательное число :', arr[index])
print(f'Общий объём памяти = {size} байт')
print('system   :', platform.system())
print('processor:', platform.processor())
print("The Python version is %s.%s.%s" % sys.version_info[:3]) 
