def even_sum_in_fib(max_val):
    a = 1
    b = 1
    total = 0
    while True:
        c = a + b
        if c >= max_val:
            return total
        if c % 2 == 0:
            total += c

        a,b = b,c

print even_sum_in_fib(4000000)