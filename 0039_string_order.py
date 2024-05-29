'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0039
-> String Order.
Enter one word and a number 'n'. 
Print the alphabet that 
in the 'n'th letter
in that word.

ex_1)           | ex_2)
Sprout          | shiftpsh
3               | 6
                |
=> r            | => p
'''

import sys

s = str(sys.stdin.readline())
i = int(sys.stdin.readline())

print(s[i-1])