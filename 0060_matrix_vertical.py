'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0060
-> Matrix Vertical

Enter 15x5 Matrix.
Read it vertically.

ex_1)
ABCDE
abcde
01234
FGHIJ
fghij

=> 
Aa0Ff Bb1Gg Cc2Hh Dd3Ii Ee4Jj

ex_2)
AABCDD
afzz
09121
a8EWg6
P5h3kx

=>
Aa0aP Af985 Bz1Eh Cz2W3 D1gk D6x
'''

mat = [input() for i in range(5)]

for row in range(15) : 
    for col in range(5) : 
        if row < len(mat[col]) : 
            print(mat[col][row], end = '')