#!/usr/bin/env python

from random import randint

path = 'input.txt'
dim_of_data = 20
low = -10
high = 10
with open(path, 'w') as f:
    arr = []
    for i in range(dim_of_data):
        arr.append(randint(low, high))
    data = ''
    for el in arr:
        data += str(el) + ' '
    f.write(data)