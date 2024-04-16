'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0019
-> Given n, finds the sum from 1 to n.
'''

# Answer 1
result = 0
n = int(input())

for i in range(1, n+1) :
    result += i

print(result)

# Answer 2
print(sum(range(1, int(input()) + 1)))