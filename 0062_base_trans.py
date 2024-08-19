'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0062
-> Base Transformation
Enter N and B. B is the base, and N is the B base.
Output the number that converted N to decimal.

ex)
ZZZZZ 36

=> 60466175
'''

n, b = input().split()

print(int(n, int(b)))