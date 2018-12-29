list = [1, 6, 5, 2, 3, 7]

a = 0
i = 0

def count_odd(list):
    a = 0
    i = 0                            
    while i < len(list):
        if list[i] % 2 != 0:
            a += 1
        i += 1 

    return a

print count_odd(list)
