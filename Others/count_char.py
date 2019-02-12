# Write a program which count and print numbers of each character in a string.
count = {}
word = " "
i = 0

while i < len(word):
    if word[i] in count:
        count[word[i]] = count[word[i]] + 1
    else:
        count[word[i]] = 1
    i +=1

print count