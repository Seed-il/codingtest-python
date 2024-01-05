start = True

while(start):
    
    try:
        a, b = map(int, input().split())

        if a > b :
            print(">")
        elif a < b :
            print("<")
        elif a == b:
            print("==")

    except:
        start = False