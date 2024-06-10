'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0043
-> String SUM.
Type a number 'n' and 
enter the 'numbers' by that 'n' 
and find the sum of those 'numbers'


ex_1)           | ex_2)
1               | 5
1               | 54321
                |
=> 1            | => 15
'''

n = input()

numbers = list(map(int, input()))

print(sum(numbers))