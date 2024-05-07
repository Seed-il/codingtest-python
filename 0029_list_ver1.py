'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0029
-> list ver1.
Enter multiple numbers and
find the number of one number(v)

ex_1)
11
1 4 1 2 4 2 4 2 3 4 4
2

=> 3
(The number of '2' is three)

ex_2)
11
1 4 1 2 4 2 4 2 3 4 4
5

=> 0
(The number of '5' is zero)
'''

import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))

v = int(sys.stdin.readline())
print(nlist.count(v))