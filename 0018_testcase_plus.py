'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0018
-> After you enter n, a, b.
Print the output of a+b n times.
'''

n = int(input())

for i in range(n) :
    a, b = map(int, input().split())
    print(a + b)