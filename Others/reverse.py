def reverse(number):
    i = number
    j = 0
    while i != 0:
        j = j * 10 + i % 10
        i = i / 10

    return j

number = 1234567890
output = reverse(number)
print output 
