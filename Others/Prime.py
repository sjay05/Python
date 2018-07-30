n = input("What is your number?: ")
is_composite = False 

for i in range(2, n):
    if n % i == 0:
        is_composite = True
        break

if not is_composite: 
    print "prime"
else:
    print "composite"
    
    
