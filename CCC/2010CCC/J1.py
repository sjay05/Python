n = input()
values = []

for i in range(1, n+1):
    if n-i not in values and n-i <= 5 and i <= 5:
        if n - i > 0 or n <= 5:
            values.append(i)

print len(values)





















# n = input()
# values = []
#
# for i in range(1, n):
#     values.append(i)
#
# if n <= 5:
#     ans = len(values) / 2 + 2
# elif n % 2 == 1:
#     ans = len(values) / 2
# else:
#     ans = len(values) / 2
#
#
# print ans

