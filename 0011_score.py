"""
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0011
-> Input a score, and classify it
(A ~ F)
"""

start = True

while(start):

    try:
        score = int(input())

        if score >= 90:
            print("A")
        elif score >= 80:
            print("B")
        elif score >= 70:
            print("C")
        elif score >= 60:
            print("D")
        else:
            print("F")

    except:
        start = False