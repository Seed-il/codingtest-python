'''
Source : Seed_il(Seed_one)
Theme : [Coding Test - Python]

Q-0046
-> String Count.


ex_1)           
Hello World
                
=> 2

ex_2)
The first character is a blank

=> 6
'''


# Solution_1
sentence = list(map(str, input().split()))
n = 0

for i in sentence : 
    n = n+1

print(n)

# Solution_2
word = input().split()
print(len(word))