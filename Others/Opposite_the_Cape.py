input = raw_input("What is your name?: ")

#First way of solving

def opposite_caps(input):
    i = 0
    d = ""
    e = ""
    list = []
    while i < len(input):
        caps = False
        low = False
        if ord(input[i]) >= 65 and ord(input[i]) < 91:
            caps = True
        else:
            low = True

        if caps == True:
            d = chr(ord(input[i]) + 32)
            list.append(d)
        else:
            e = chr(ord(input[i]) - 32)
            list.append(e)

        i += 1

    s = ""
    b = ""
    for b in list:
        s += b

    return "Output1 = ", s

print opposite_caps(input)


# Second way of solving
g = ""
i = 0

while i < len(input):
    if ord(input[i]) >= 65 and ord(input[i]) < 91:
        d = chr(ord(input[i]) + 32)
        g += d
    else:
        e = chr(ord(input[i]) - 32)
        g += e

    i += 1

print "Output2 = ", g






