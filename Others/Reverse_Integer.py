num = 1234576

def reverse_int(a):
    b = 0 
    k = 0    
    while a != 0:
        b = a % 10
        a = a / 10
        k = k * 10 + b
        
    return k

print reverse_int(num)
