# Iterative
n = input("Number?: ")

# #version1
# def power_of_two(n):
#     while True:
#         if n / 2 == 0:
#             return "The number is a power of 2."
#         elif n % 2 != 0:
#             return "The number is not a power of 2."
#         else:
#             n = n / 2
#
# print power_of_two(n)
#
#
# #version2
# def powerof2(n):
#     while n > 1 and n % 2 == 0:
#         print "Hmmmm ;( n = %s" % n
#         n = n/2
#
#     return n == 1
#
# print powerof2(n)


# Using Bitwise operator - &
print n & (n-1) == 0
















