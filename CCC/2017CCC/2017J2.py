n = input("N-Value?")
k = input("K-value?")

def shifty_sum(n, k):
    a = n
    for i in range(1, k+1):
        n = n * 10 
        a = a + n
    return a

print shifty_sum(n, k)


