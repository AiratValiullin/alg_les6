# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

from random import randint

lst = [randint(0, 20) for i in range(5)]
min1 = 20
min2 = 20
print(lst)
for i in lst:
    if min1 > i:
        min1 = i

lst2 = lst[:lst.index(min1)]+lst[lst.index(min1)+1:]

for i in lst2:
    if min2 > i:
        min2 = i

print(f' Первое минимальное число {min1}')
print(f' Второе минимальное число {min2}')

# 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] win32
#  type = <class 'list'>, size = 68, object= [3, 18, 12, 16, 4, 8]
# 	 type = <class 'int'>, size = 14, object= 3
# 	 type = <class 'int'>, size = 14, object= 18
# 	 type = <class 'int'>, size = 14, object= 12
# 	 type = <class 'int'>, size = 14, object= 16
# 	 type = <class 'int'>, size = 14, object= 4
# 	 type = <class 'int'>, size = 14, object= 8
#  type = <class 'list'>, size = 56, object= [18, 12, 16, 4, 8]
# 	 type = <class 'int'>, size = 14, object= 18
# 	 type = <class 'int'>, size = 14, object= 12
# 	 type = <class 'int'>, size = 14, object= 16
# 	 type = <class 'int'>, size = 14, object= 4
# 	 type = <class 'int'>, size = 14, object= 8
#  type = <class 'int'>, size = 14, object= 3
#  type = <class 'int'>, size = 14, object= 4
# Вывод: Минусы первого варианта в том, что создаются два списка.

import sys
print(sys.version, sys.platform)
def show_size(x, level = 0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object= {x}')

    if  hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                 show_size(xx, level + 1)

show_size(lst)
show_size(lst2)
show_size(min1)
show_size(min2)


