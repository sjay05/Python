n = 148
k = 4

#iterative function to calculate sum of digits of a number multiple times until Value == 1
def sum_int(word):
    value = 0
    for i in range(len(word)):
        value += int(word[i])
    
    return value

main = sum_int(str(n)*k)
while True:
    if len(str(main)) == 1:
        print main
        break
    else:
        main = sum_int(str(main))

#recursive function to calculate sum of digits in a number
def int_sum(number):
    if len(str(number)) == 1:
        return number
    else:
        return int(str(number)[0]) + int_sum(int(str(number)[1:]))

print int_sum(123)
