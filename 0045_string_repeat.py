'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0045
-> String repeat.
Enter the number of tests 
Enter the number of repetitions and words. 
Repeat and output the number of characters 
as many times as the tests.

ex_1)           
2
3 ABC
5 /HTP                       
                
=> 
AAABBBCCC
/////HHHHHTTTTTPPPPP
'''


case = int(input())

for i in range(0, case) : 
    s = list(map(str, input().split()))
    n = int(s[0])
    for j in s[1] :
        for k in range(0, n) :
            print(j, end='')
    print()