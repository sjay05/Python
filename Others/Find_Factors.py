


def print_factors(x):
   count = 0
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
          count = count + 1                                                                     
          print(i)
             
   print("Number of factors:%s" % count)

num = input("What is your number?: ")
print_factors(num)

