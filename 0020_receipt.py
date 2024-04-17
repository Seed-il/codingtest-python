'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0020
-> Check Receipt
Compare the total amount of the receipt
with the price purchased
by item and the value calculated by quantity
'''

total = int(input()) # total amount

n = int(input()) # number of items

result = 0
for i in range(n) :
    # items and counts
    a, b = map(int, input().split())
    result = result + a * b

if result == total : # compare
    print("Yes")
else :
    print("No")


'''
ex1)
260000
4
20000 5
30000 2
10000 6
5000 8

=> Yes

ex2)
250000
4
20000 5
30000 2
10000 6
5000 8

=> No
'''