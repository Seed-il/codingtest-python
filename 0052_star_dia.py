'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0052
-> Star - Diamond.
Input a number.
Print Star Diamond.

ex)
5

=>
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

n = int(input())

for i in range(1, n) : 
    print(' ' * (n-i) + '*' * (2 * i - 1))

for j in range(n, 0, -1) : 
    print(' ' * (n-j) + '*' * (2 * j -1))