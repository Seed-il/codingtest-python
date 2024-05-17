'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0032
-> list ver4.
Enter 9 numbers and 
print out the maximum number
and the order

ex_1)
3
29
38
12
57
74
40
85
61

=>
85
8
'''

'''
무조건적으로 9개의 수를 \n에 의거하여 저장하는 list를 만들어야 한다.
max(nlist)와 nlist[max(nlist)]를 구해야한다.
'''

import sys

nlist = []

for i in range(0, 9) : 
    nlist.append(int(sys.stdin.readline()))

maxnum = max(nlist)

print(maxnum)
print(nlist.index(maxnum) + 1)