'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0048
-> String Dial.
Old dial phones have to move 
the number they want to press clockwise.
It takes about 2 seconds to move the number 1. 
Then it increases by 1 second from the number.
From the second, the alphabet is written. 
Enter the alphabet to calculate the total time it takes.


ex_1)           
WA
                
=> 13
---------------
ex_2)
UNUCIC

=> 36
'''

dial = ['ABC', 'DEF', 'GHI', 'JKL',
        'MNO', 'PQRS', 'TUV', 'WXYZ']

res = 0

n = input()

for i in range(len(n)) : 
    for j in dial : 
        if n[i] in j : 
            res += dial.index(j) + 3
print(res)