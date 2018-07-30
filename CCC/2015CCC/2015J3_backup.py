import string

alphabet = list(string.ascii_lowercase)
input = "abc"
print alphabet

# Down below are the variables
l = 0
p = 0
a = ord('a')
e = ord('e')
i = ord('i')
o = ord('o')
u = ord('u')
list_of_vowels = [a, e, i, o, u]
print list_of_vowels
vowels = ['a', 'e', 'i', 'o', 'u']
final_list = []

while l < len(alphabet):
    if alphabet[l] not in vowels and alphabet[l] in input:
        var = ord(input[l])
        new_var = 0
        while p < len(list_of_vowels):
            if list_of_vowels[p] > var:
                new_var = list_of_vowels[p] - var
                final_list.append(new_var)
                p += 1
            elif list_of_vowels[p] < var:
                new_var = var - list_of_vowels[p]
                final_list.append(new_var)
                p += 1
    l += 1

f = 0
g = 0
h = 0
aq = 0
bq = 0
ch = 0
while f < len(input):
    if input[f] not in vowels:
        g = input[f]
        h = chr(ord(input[f]) - final_list[0])
        if list.index(input[f]) + 1 not in vowels:
            aq = alphabet[list.index(input[f])]
        else:
            aq = alphabet[list.index(input[f]) + 1]

    bq = g + h + aq
    ch = ch + bq
    f += 1

print ch








