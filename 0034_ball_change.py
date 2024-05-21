'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0034
-> ball change.
Enter the number of baskets and the number of balls exchanged. 
Each basket contains a ball with its own number on it. 
Exchange the balls in each basket as many times as they were exchanged, 
and print out the number of balls in the basket at the end.

ex_1)
5 4
1 2
3 4
1 4
2 2  

=> 3 1 4 2 5
'''

'''
n과 m을 입력한다.
n은 바구니의 개수,
m은 공을 교환하는 작업의 개수이다.
처음엔 각 바구니에 각 바구니 순번이 적힌 공이 들어있다.
i와 j번 바구니 속의 공을 m번만큼 서로 교환한다.
각 바구니마다 마지막에 넣은 공을 출력한다.
'''

import sys

n, m = map(int, sys.stdin.readline().split())

nlist = []

for t in range(0, n) : 
    nlist.append(t+1)

for i in range(0, m) : 
    a, b = map(int, sys.stdin.readline().split())
    tmp1 = nlist[a-1]
    tmp2 = nlist[b-1]
    nlist[a-1] = tmp2
    nlist[b-1] = tmp1

for res in nlist : 
    print(res, end=' ')