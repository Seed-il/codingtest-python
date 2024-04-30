'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0027
-> Print Test Case - A+B
until a, b = 0
'''

import sys

while(True) : 
    a, b = map(int, sys.stdin.readline().split())
    if(a == 0 & b == 0) :
        break; 
    print(a+b)


'''
1 1
2 3
3 4
9 8
5 2
0 0

=>
2
5
7
17
7
'''