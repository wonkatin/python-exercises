# Write a function to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example function call
#
# factorial(5)
#
# > 120
#
n = 23
fact = 1
for i in range(1,n+1):
    fact = fact * i
print ("The factorial of 23 is : ",end="")
print (fact)

def factorial(n):
    total = 1
    for i in range(1, n + 1):
        print(f'i is {i} total is {total}')
        total *= i
        
    return total

solv = factorial(5)
print(solv)