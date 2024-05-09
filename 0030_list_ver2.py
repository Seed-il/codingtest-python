'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0030
-> list ver2.
Enter multiple numbers and 
print out numbers less than v

ex_1)
10 5
1 10 4 9 2 3 8 5 7 6

=> 1 4 2 3
'''

import sys

n, v = map(int, sys.stdin.readline().split())

nlist = list(map(int, sys.stdin.readline().split()))

for i in nlist : 
    if i < v : 
        print(i, end=' ')