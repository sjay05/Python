x = input("Word?")
count = 0
for c in x:
    if c in ["a", "e", "i", "o", "u"]:
        count = count + 1

print count
    
