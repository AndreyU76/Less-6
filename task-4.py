import sys
import platform

n = int(input("введи данные n: "))
a = 0
for i in range(1,n+1):
    a += i
m = n * (n + 1) // 2
#print(a)
#print(m)


def show_size(x, level=0):
    print ('\t' * level, x.__class__, sys.getsizeof(x), x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        else:
            for xx in x:
                show_size(xx, level + 1)


#print(sys.getsizeof(n))
print(f'Общий объём памяти = {sys.getsizeof(a)} байт')
print(f'Общий объём памяти = {sys.getsizeof(n)} байт')
print(f'Общий объём памяти = {sys.getsizeof(m)} байт')
show_size(n)

print (sys.platform)
print (sys.version)
