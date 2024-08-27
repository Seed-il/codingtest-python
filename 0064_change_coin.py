'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0064
-> Change coin
Enter your change and 
find the number of coins 
that should be in each type
 - Quater : $0.25
 - Dime : $0.10
 - Nickel : $0.05
 - Penny : $0.01

ex)
3
124
25
194

=> 
4 2 0 4
1 0 0 0
7 1 1 4
'''
from sys import stdin
input = stdin.readline

quater = 25
dime = 10
nickel = 5
penny = 1

n = int(input())

changeList = []
for i in range(n) : 
    changeList.append(int(input()))

for list in changeList : 
    res1 = int(list / quater)
    res2 = int(list % quater / dime)
    res3 = int(list % quater % dime / nickel)
    res4 = int(list % quater % dime % nickel / penny)

    print(res1, res2, res3, res4)