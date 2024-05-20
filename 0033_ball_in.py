'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0033
-> ball in.
Enter the number of baskets 
and the number of times balls were put in the baskets. 
The work consists of i, j, and k, 
and puts balls of the number k, from baskets i to j. 
Finally, print out the balls in the baskets.

ex_1)
5 4
1 2 3   
3 4 4   
1 4 1   
2 2 2   

=> 1 2 1 1 0
'''

'''
n과 m을 입력한다.
n은 바구니의 개수,
m은 공을 넣는 작업의 개수이다.
i번부터 j번까지 k번 공을 넣는다.
각 바구니마다 마지막에 넣은 공을 출력한다.(없으면 0)
'''

import sys

n, m = map(int, sys.stdin.readline().split())

nlist = []

for t in range(0, n) : 
    nlist.append(0)

for i in range(0, m) : 
    a, b, c = map(int, sys.stdin.readline().split())

    for j in range(a-1, b) : 
        nlist[j] = c

for res in nlist : 
    print(res, end=' ')