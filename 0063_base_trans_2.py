'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0063
-> Base Transformation 2


ex)
60466175 36

=> ZZZZZ
'''

arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, input().split())
res = ""

while n:
    res += str(arr[n % b])
    n //= b

print(res[::-1])