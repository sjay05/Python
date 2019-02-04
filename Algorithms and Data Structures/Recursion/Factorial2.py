n = input("What is your number?:")

# Iterative way of finding factorial
def find_factorial(n):
     fact = 1
     for i in range(2, n+1):
         fact = fact * i
     return fact

# Recursive way of finding factorial
def factorial(n):
    if n == 1:
       return n
    return n * factorial(n-1)


#print find_factorial(n)

print factorial(n)


"""
5!
5 * factorial(4)
      4 * factorial(3)
            3 * factorial(2)
                  2 * factorial(1)
"""


