'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0022
-> Fast input & A + B
Use the "sys.stdin" function
instead of the "input()" function.
"sys.stdin" function is faster
and memory-efficient.
'''

import sys

n = int(sys.stdin.readline())

for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)


'''
5
1 1
12 34
5 500
40 60
1000 1000

=>
2
46
505
100
2000
'''