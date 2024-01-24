'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0013
-> Quadrant
'''

while(True):
    x, y = map(int, input().split())

    if(x > 0 and y > 0):
        print(1)
    elif(x < 0 and y > 0):
        print(2)
    elif(x < 0 and y < 0):
        print(3)
    else:
        print(4)