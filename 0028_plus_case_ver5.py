'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0028
-> Test Case A + B ver5
If you receive two numbers(A, B), 
constantly print out the values of the A + B. 
If you do not receive two numbers, exit the program.
'''

import sys

while(True) : 
    try : 
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except :  # 예외 발생 시 while문을 빠져나가고 프로그램이 종료된다.
        break


'''
1 1
2 3
3 4
9 8
5 2
 

=>
2
5
7
17
7
'''