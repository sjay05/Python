n = input("What is n daddy?: ")
values = []

for i in range(1, n):
    values.append(i)

print values

if n <= 5:
    ans = len(values) / 2 + 2
elif n % 2 == 1:
    ans = len(values) / 2
else:
    ans = len(values) / 2


print ans



