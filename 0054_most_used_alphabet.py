'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0054
-> Most used alphabet.

Enter a word. 
Print the alphabet that is most commonly used in the word. 
If there are multiple alphabets that are most used, print "?"

ex_1)           
Mississipi
                
=> ?

ex_2)           
zZa
                
=> Z

ex_3)           
baaa
                
=> A
'''

word = str(input()).upper()
wlist = list(set(word))

cnt = []
for i in wlist : 
    alphabet = word.count(i)
    cnt.append(alphabet)

if cnt.count(max(cnt)) > 1 :
    print("?")
else : 
    print(wlist[(cnt.index(max(cnt)))])