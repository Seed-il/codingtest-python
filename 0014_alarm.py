'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0014
-> Set an alarm 45 minutes earlier 
than the given time
'''

h, m = map(int, input().split()) #시간과 분을 입력받는다.

m_re = m - 45 # 분에서 45를 뺀다.
if(m_re < 0): # 45를 뺀 분이 음수일 경우
    m_re = 60 + m_re # 60분을 더하고,
    h = h-1 # 시간은 1시간을 뺀다.
    if(h < 0): # 1시간을 뺀 시간이 음수라면
        h = 24 + h # 24시간을 더해준다.

print(h, m_re)
