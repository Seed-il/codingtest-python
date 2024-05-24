'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0036
-> List Divide.
Enter any number of 10,
Divide 42 into each number and get the rest.
Print out how many different values there are.

ex_1)     |   ex_2)     |   ex_3)
1         |   42        |   39
2         |   84        |   40
3         |   252       |   41
4         |   420       |   42
5         |   840       |   43
6         |   126       |   44
7         |   42        |   82
8         |   84        |   83
9         |   420       |   84
10        |   126       |   85
          |             |   
=> 10     |   => 1      |   => 6
'''

'''
임의의 수 10개를 42로 나눈 나머지를 리스트에 저장하고,
리스트에 중복된 것들을 제외한 나머지 개수를 출력
'''

import sys

nlist = []

for i in range(0, 10) : 
    nlist.append((int(sys.stdin.readline())) % 42)

print(len(set(nlist))) #set 함수는 중복을 제거하되, 순서가 정렬되지 않는다.