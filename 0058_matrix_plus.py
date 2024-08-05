'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0058
-> Matrix plus

Enter two (NxM) Matrixs.
And plus them.

ex)
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100

=> 
4 4 4
6 6 6
5 6 100
'''

m1, m2 = [], []

n, m = map(int, input().split())

for row in range(n) : 
    row = list(map(int, input().split()))
    m1.append(row)

for row in range(n) : 
    row = list(map(int, input().split()))
    m2.append(row)

for row in range(n) : 
    for col in range(m) : 
        print(m1[row][col] + m2[row][col], end = ' ')
    print()