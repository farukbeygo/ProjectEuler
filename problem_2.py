"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

# I will write a function that return sum of the even-valued terms of Fibonacci sequence for given number

def fib_evenSum(x):
    evenSum = 0
    number_a, number_b = 1, 1
    while number_a<x:
        number_a, number_b = number_b, number_a
        number_a+=number_b
        if number_a%2 == 0:
            evenSum+=number_a
    return evenSum

