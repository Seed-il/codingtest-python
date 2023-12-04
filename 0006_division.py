a, b, c = map(int, input().split())

d1_1 = (a+b)%c
d1_2 = ((a%c) + (b%c)) % c

d2_1 = (a*b)%c
d2_2 = ((a%c) * (b%c)) % c

print(d1_1)
print(d1_2)
print(d2_1)
print(d2_2)
