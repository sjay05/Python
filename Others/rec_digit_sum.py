n = 123
k = 3

# recursive function to to calculate sum of digits multiple times until value == 1.
def digit_sum(value):
    if len(str(value)) == 1:
        print value
    else:
        value = int_sum(int(value))
        digit_sum(value)

# recursive function to calculate sum of digits
def int_sum(number):
    if len(str(number)) == 1:
        return number
    else:
        return int(str(number)[0]) + int_sum(int(str(number)[1:]))

digit_sum(str(n)*k)
