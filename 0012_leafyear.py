'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0012
-> Print 1 or 0 if it is a leap year when given a year.
Leap year is when the year is a multiple of 4, not a multiple of 100, 
or a multiple of 400.
'''

year = int(input())

if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print(1) # leap year
else:
    print(0) # not leap year