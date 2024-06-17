'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0047
-> String Reverse.
Input two numbers,
and reverse each other.
Print out the bigger.


ex_1)           
734 893
                
=> 437
---------------
ex_2)
221 231

=> 132
'''

n, m = input().split()
n = int(n[::-1])
m = int(m[::-1])

print(n) if n > m else print(m)