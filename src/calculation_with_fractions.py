# Write your solution here


from fractions import *


def fractionate(amount):
    fractions = []
    for i in range(amount):
        fractions.append(Fraction(1, amount))

    return fractions
