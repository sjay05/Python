x = input("What is your sentence?")
y = input("What is your word?")

if y in x.split(" "):
    print "Y"
else:
    print "not found"
