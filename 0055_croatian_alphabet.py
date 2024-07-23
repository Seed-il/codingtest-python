'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0055
-> Croatian alphabet.
Enter the alphabet and special characters, 
and print out how many Croatian alphabets 
were used in total.

ex_1)           | ex_2)
ljes=njak       | ddz=z=
                |
=> 6            | => 3
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
ex_3)           | ex_4)
nljj            | c=c=
                |
=> 3            | => 2
'''

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for i in croatia : 
    word = word.replace(i, '*')

print(len(word))