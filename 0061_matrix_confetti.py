'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0061
-> Matrix confetti
Enter the number of confetti. 
Enter the location of each confetti.
Find the area of the area 
where the confetti is located.

ex)
3
3 7
15 7
5 2

=> 
260
'''
from sys import stdin
input = stdin.readline

paper = [[0] * 101 for _ in range(101)]

n = int(input())

for i in range(n) : 
    x, y = map(int, input().split())

    for row in range(x, x + 10) : 
        for col in range(y, y + 10) : 
            paper[row][col] = 1

res = 0
for i in paper : 
    res += sum(i)

print(res)