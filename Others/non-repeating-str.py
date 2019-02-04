# Finding the first letter that doesn't repeat...
word = "ccAyfftthhyA"
word_list = []

for i in range(len(word)):
    if word[i] in word_list:
        word_list.remove(word[i])
    else:
        word_list.append(word[i])

if len(word_list) == 0:
    print "All the letters appear more than once."
else:
    print word_list[0]

