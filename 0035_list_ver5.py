'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0035
-> List ver5.
Enter 8 numbers from 1 to 10, 
and output the remaining 2 numbers 
that you did not enter.

ex_1)
3
1
4
5
7
9
6
10

=> 
2
8
'''

'''
1부터 10까지의 리스트를 먼저 생성하고
8개의 숫자를 입력할 때마다 리스트에서 제거해준다.
'''

import sys

alist = list(range(1, 11, 1))

for i in range(0, 8) : 
    num = int(sys.stdin.readline())
    alist.remove(num)

alist.sort
for res in alist : 
    print(res)