'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0013
-> Quadrant
'''

while(True):
    x, y = map(int, input().split())

    if(x > 0 and y > 0):
        print(1) # 1quadrant
    elif(x < 0 and y > 0):
        print(2) # 2quadrant
    elif(x < 0 and y < 0):
        print(3) # 3quadrant
    elif(x > 0 and y < 0):
        print(4) # 4quadrant