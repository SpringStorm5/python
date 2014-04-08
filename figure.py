#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
rows = int(input('Введите количество строк в фигуре: '))
 
first_line = last_line = ('* ' * rows)[:-1]
 
print(first_line)
for r in range(rows-2):
    print('{0}{1}{0}'.format('*', ' '*((rows-2)*2+1)))
print(last_line)
 
for r in range(rows+1):
    print('* '*r)
 