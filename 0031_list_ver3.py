'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0031
-> list ver3.
Enter multiple numbers and 
print out numbers minimum and maximum

ex_1)
5
20 10 35 30 7

=> 7 35
'''

import sys

n = int(sys.stdin.readline())

nlist = list(map(int, sys.stdin.readline().split()))

print(min(nlist), max(nlist))