'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0042
-> String ASCII.
Input a word, 
and print out 
the ASCII code about the word.

ex_1)           | ex_2)
A               | C
                |
=> 65           | => 67
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
ex_3)           | ex_4)
0               | a
                |
=> 48           | => 97
'''

import sys 

n = sys.stdin.readline().rstrip()

print(ord(n))