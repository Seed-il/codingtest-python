"""
Source : Seed_il(Seed_one)

Theme : [Coding Test - Python]

Q-0010
-> Input two numbers A, B
and Compare them
"""

start = True

while(start):

    try:
        a, b = map(int, input().split())

        if a > b:
            print(">")
        elif a < b:
            print("<")
        elif a == b:
            print("==")

    except:
        start = False