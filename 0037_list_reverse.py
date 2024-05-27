'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0037
-> bascket reverse.
Enter n and m.
n is the number of baskets,
m is the number of tasks that reverse the order of the basket.
The work of changing the baskets in the i-th to j-th 
in reverse order.
Repeat m times.

ex_1)
5 4
1 2
3 4
1 4
2 2  

=> 3 4 1 2 5
'''

'''
n과 m을 입력한다.
n은 바구니의 개수,
m은 바구니의 순서를 역순으로 바꾸는 작업의 개수이다.
i번째부터 j번째에 있는 바구니들을 역순으로 바꾸는 작업을 
m번 반복한다.
'''

import sys

n, m = map(int, sys.stdin.readline().split())

nlist = []

for t in range(0, n) : 
    nlist.append(t+1)

for cnt in range(0, m) : 
    i, j = map(int, sys.stdin.readline().split())

    tmp = nlist[i-1:j]
    tmp.reverse()

    nlist[i-1:j] = tmp

for n in range(n) : 
    print(nlist[n], end = ' ')