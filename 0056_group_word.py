'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0056
-> Group word.
Enter a number and enter as many words as that number. 
Find the total number of group words.
groupword : aaa, abb, cca, ...

ex_1)   
3        
happy
new
year
                
=> 3

ex_2)           
4
aba
abab
abcabc
a
                
=> 1

ex_3)           
5
ab
aa
aca
ba
bb
                
=> 4
'''

case = int(input())
cnt = case

for i in range(case) : 
    word = str(input())
    for j in range(0, len(word)-1) : 
        if(word[j] == word[j+1]) : 
            pass
        elif word[j] in word[j+1:] : 
            cnt -= 1
            break
print(cnt)