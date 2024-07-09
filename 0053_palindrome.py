'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0053
-> Palindrome.
Input a word.
Check it is Palindrome or not.

ex_1)
level

=> 1

ex_2)
online

=> 0
'''

n = str(input())

nlist = list(n)
nlist.reverse()
n_rev = ''.join(nlist)

if(n == n_rev) : 
    print(1)
else : 
    print(0)