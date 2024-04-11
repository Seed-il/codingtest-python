'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0016
-> Throw three dice with eyes from 1 to 6 
and calculate the prize money according to the following rule.

 - If you get 3 same eyes, it's 10,000 won + (same eyes) x 1,000 won
 - If there are only two same eyes, it's 1,000 won + 100 won
 - If all eyes are different (the biggest of them) x 100 won
'''
a, b, c = map(int, input().split())

if a == b == c :
    print(10000 + a * 1000)
elif a == b :
    print(1000 + a * 100)
elif a == c :
    print(1000 + a * 100)
elif b == c :
    print(1000 + b * 100)
else :
    print(100 * max(a, b, c))


'''
3 3 6 => 1300
2 2 2 => 12000
6 2 5 => 600
'''