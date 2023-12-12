# 두 개의 세자리 자연수를 곱하면 다음과 같이 이루어진다.
#       4 7 2
#     X 3 8 5
# ------------
#     2 3 6 0
#   3 7 7 6
# 1 4 1 6
# ------------
# 1 8 1 7 2 0
#
# 위의 과정을 순차적으로 출력하시오.

"""
while True:
    try:
        a = int(input())
        b = int(input())

        if(100 <= a <= 999 and 100 <= b <= 999):
            b1 = b % 100 % 10 # b의 첫째 자리수
            b2 = b % 100 - b1 # b의 둘째 자리수
            b3 = b - b1 - b2 # b의 셋째 자리수

            result1 = a * b1
            result2 = a * b2
            result3 = a * b3

            print(result1)
            print(result2)
            print(result3)
            print(result1 + result2 + result3)
            break

        else:
            #print("Input Correct1")
            break

    except:
        #print("Input Correct2")
        break

"""


a = int(input())
b = input()

print(a * (int(b[2])))
print(a * (int(b[1])))
print(a * (int(b[0])))
print(a * int(b))


"""
a = int(input())
b = int(input())

b1 = b % 100 % 10 # b의 첫째 자리수
b2 = b % 100 - b1 # b의 둘째 자리수
b3 = b - b1 - b2 # b의 셋째 자리수

result1 = a * b1
result2 = a * b2
result3 = a * b3

print(result1)
print(result2)
print(result3)
print(result1 + result2 + result3)
"""
