"""
"The following problem is taken from Project Euler."

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

#that was very basic problem
square_num = 0
square_list = []

for num in range(1, 101):
    square_list.append(num*num)
    square_num+=num

difference = square_num**2 - sum(square_list)
print(difference)
