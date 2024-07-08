'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0051
-> Chess.
The chess piece consists of 
1 king, 1 queen, 2 looks, 
2 bishops, 2 nights, and 8 phones.

Find the number of pieces present, 
and how much more or less should be added.
'''

'''
ex_1)
0 1 2 2 2 7

=> 1 0 0 0 0 1

ex_2)
2 1 2 1 2 1

=> -1 0 0 1 0 7
'''

chess = [1, 1, 2, 2, 2, 8]

n = list(map(int, input().split()))

for i in range(0, 6) : 
    print(chess[i] - n[i], end = ' ')