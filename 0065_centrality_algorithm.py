'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0065
-> Centrality Algorithm
Place a point in the center of each side of the square 
and connect it between the points to make small squares. 
Find the number of points needed 
according to this number of times.
*─────*
│     │  
│     │
*─────*
*──*──*
│  │  │
*──*──*
│  │  │
*──*──*

ex_1)
1

-> 9

ex_2)
2

-> 25
'''

from sys import stdin
input = stdin.readline

n = int(input())

print((2 ** int(n) + 1) ** 2)