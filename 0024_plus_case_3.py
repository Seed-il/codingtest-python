'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0024
-> Test Case A + B ver2
Print it out in the following format.
Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5 ...
'''

import sys

t = int(sys.stdin.readline())

for i in range(t) : 
    a, b = map(int, sys.stdin.readline().split())

    print("Case #%d: %d + %d = %d" %(i + 1, a, b, a+b))


'''
5
1 1
2 3
3 4
9 8
5 2

=>
Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7
'''