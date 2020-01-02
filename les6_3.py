# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

from random import randint

lst = [randint(0, 20) for i in range(5)]
min1 = 20

print(lst)
for i in lst:
    if min1 > i:
        min1 = i

print(f' Первое минимальное число {min1}')

lst.pop(lst.index(min1))

for i in lst:
    if min1 > i:
        min1 = i

print(f' Первое минимальное число {min1}')


 # type = <class 'list'>, size = 68, object= [4, 14, 13, 15]
	#  type = <class 'int'>, size = 14, object= 4
	#  type = <class 'int'>, size = 14, object= 14
	#  type = <class 'int'>, size = 14, object= 13
	#  type = <class 'int'>, size = 14, object= 15
 # type = <class 'int'>, size = 12, object= 0
 # type = <class 'int'>, size = 14, object= 4
# Вывод: В данном варианте исключили второй список и одну переменную, соответсвенно памяти затратилось меньше.
# Данный вариант оптимальный, т.к. решает поставленную задачу и использует минимальный объем памяти.

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
show_size(min1)

