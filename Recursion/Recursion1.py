#Factorial Program (Recursion)

def recur_factorial(n):
    if n == 1:
        return n
    else:
        result = recur_factorial(n-1)
        return n * result

print recur_factorial(5)