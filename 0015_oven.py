'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0015
-> Calculate what time 
the oven timer ends
'''

h, m = map(int, input().split()) # 첫째 줄에 시, 분 입력
oven = int(input()) # 둘째 줄에 원하는 오븐 타이머를 입력

t1 = m + oven # 분에 오븐 타이머를 더해준다.
t2 = int(t1 / 60) # 더해준 값에 60을 나눈 몫

r1 = h + t2 # 출력값 중 시
r2 = t1 - t2 * 60 # 출력값 중 분

if(r1 >= 24): # 출력값 중 시가 24 이상이면 24를 빼준다.
    r1 = r1 - 24

print(r1, r2)