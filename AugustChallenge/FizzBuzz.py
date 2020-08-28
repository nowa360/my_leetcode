# coding=utf-8
"""
August 26 Challenge - Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

"""


def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []

    for i in xrange(1, n + 1):
        if i % 3 == i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res
