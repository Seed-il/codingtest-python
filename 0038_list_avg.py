'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0038
-> List Average.
Enter the number of test takers and the test score. 
Divide the score by the highest score and 
multiply by 100 to derive the average value again.

ex_1)           | ex_2)
3               | 3
40 80 60        | 10 20 30
                |
=> 75.0         | => 66.666667
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
ex_3)           | ex_4)
4               | 5
1 100 100 100   | 1 2 4 8 16 
                |
=> 75.25        | => 38.75
'''

import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))

maxScore = max(nlist)

slist = []
for score in range(n) : 
    slist.append(nlist[score] / maxScore * 100)

print(sum(slist) / n)