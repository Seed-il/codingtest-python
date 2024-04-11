'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0017
-> After you enter n,
print the stages of the multiplication table n.
'''

n = int(input())

a = range(1, 10) # 1~9

for i in a :
    print(n, "*", i, "=", n*i)