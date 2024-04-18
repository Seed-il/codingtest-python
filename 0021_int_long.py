'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0021
-> Integer Data Type
Enter a multiple of 4 "n",
and print "long" by the quotient of "n" divided by four
'''

n = int(input())

cnt = int(n / 4)

for i in range(cnt) :
    print("long", end=" ")

print("int")

'''
ex1)
4

=> long int

ex2)
20

=> long long long long long int
'''