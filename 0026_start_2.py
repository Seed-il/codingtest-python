'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0026
-> Print Stars ver2
'''

import sys

n = int(sys.stdin.readline())

for i in range(1, n+1) :

    print(" " * (n-i) + "*" * i)
   
    
'''
5

=>
    *
   **
  ***
 ****
*****
'''