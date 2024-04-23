'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0023
-> Test Case A + B ver2
Print it out in the following format.
Case #1: 2
Case #2: 5 ...
'''

import sys

t = int(sys.stdin.readline())

for i in range(t) :
    a, b = map(int, sys.stdin.readline().split())

    print("Case #%d: %d" %(i +1, a + b))



'''
5
1 1
2 3
3 4
9 8
5 2

=>
Case #1: 2
Case #2: 5
Case #3: 7
Case #4: 17
Case #5: 7
'''