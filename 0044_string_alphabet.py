'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0044
-> String alphabet.
Type one lowercase alphabet word 
and print out the order 
in which each alphabet is located.
 For non-existent alphabets, print '-1'


ex_1)           
apple                           
                
=> 
0 -1 -1 -1 4 -1 -1
-1 -1 -1 -1 3 -1 -1
-1 1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1
'''

# Solution_1
n1 = list(input())

c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in n1 : 
        print(n1.index(i), end = ' ')
    else:
        print(-1, end = ' ')

print()
# Solution_2
n2 = input()

for i in 'abcdefghijklmnopqrstuvwxyz':
    print(n2.find(i), end = ' ')