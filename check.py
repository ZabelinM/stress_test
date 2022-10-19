#!/usr/bin/env python

path1 = 'out1.txt'
path2 = 'out2.txt'

out_path = 'diff.txt'
input_path = 'input.txt'

with open(path1, 'r') as f1:
    res1 = f1.read()

with open(path2, 'r') as f2:
    res2 = f2.read()


if res1 != res2:
    with open(input_path, 'r') as i:
        input_data = i.read()
    with open(out_path, 'a') as out:
        out.write(f'algo 1 res is :  \n {res1} \n')
        out.write(f'algo 2 res is :  \n {res2} \n')
        out.write(f'input data is : \n {input_data} \n')
        out.write('--------------------------- \n')

