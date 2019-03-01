# Solution to problem:
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342
(three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
'''

singleint = {'1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4}

tens_dict = {'0': 3, '1': 6 , '2': 6, '3': 8, '4': 8, '5': 7, '6': 7, '7': 9, '8': 8, '9': 8}

secondary_tens = {'2': 6, '3': 6, '4': 5, '5': 5, '6': 5, '7': 7, '8': 6, '9': 6}

base_10 = {'3': 7, '4': 8}

x = 1000

def calc(value):
    count = 0
    i = 0
    b10 = len(value)
    if len(value) >= 3:
        if value[len(value)-2] != '0' or value[len(value)-1] != '0':
            count += 3
    while i < len(value):
        if len(value) == 1:
            count += singleint.get(value[0])
            break
        if i == len(value)-2:
            if value[i] == "0":
                if value[i+1] == "0":
                    break
                else:
                    count += singleint.get(value[i+1])
                    break
            if value[i] == "1":
                count += tens_dict.get(value[i+1])
                break
            elif value[i+1] == "0":
                count += secondary_tens.get(value[i])
                break
            else:
                count += secondary_tens.get(value[i])
                count += singleint.get(value[i+1])
                break

        else:
            if i == len(value)-1 and value[i] == "0":
                break
            elif i == len(value)-1 and value[i] != "0":
                count += singleint.get(value[i])
                b10 -= 1
                i += 1
                break
            elif value[i+1] == "0":
                count += singleint.get(value[i])
                count += base_10.get(str(b10))
                i += 2
                b10 -= 1
            else:
                count += singleint.get(value[i])
                count += base_10.get(str(b10))
                b10 -= 1
                i += 1

    return count

print calc(str(x))


# main_count = 0
# i = 1
# while i <= x:
#     temp = calc(str(i))
#     main_count += int(temp)
#     i += 1
#
# print main_count

