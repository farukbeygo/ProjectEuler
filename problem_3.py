"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import math

number = 600851475143
num_list = []
div_list = []
pri_list = []


for num in range(2, round(math.sqrt(number))):
    num_list.append(num)

for div in num_list:
    if number%div == 0:
        div_list.append(div)


for pri in div_list:
    flag = True
    for pri_div in range(2, round(math.sqrt(pri))):
        if pri%pri_div == 0:
            flag = False
            break
    if flag:
        pri_list.append(pri)
            
print(max(pri_list))