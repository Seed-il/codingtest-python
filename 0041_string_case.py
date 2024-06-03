'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0041
-> String Case.
Input a word, 
and print out 
the fisrt letter and last letter
of this word.
'''

'''
ex_1)
3
ABCDE
O
AB

=> 
AE
OO
AB
'''

import sys

n = int(sys.stdin.readline())

for i in range(n) : 
    s = str(sys.stdin.readline())
    print(s[0] + s.strip()[-1])