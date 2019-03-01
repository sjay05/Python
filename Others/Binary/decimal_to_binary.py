# Decimal number to binary number conversion code.
n = input("Decimal Number: ")
binary = []
while True:
    if n > 1:
        binary.append(n % 2)
        n = n / 2
    else:
        binary.append(1)
        break

binary.reverse()
print binary                  