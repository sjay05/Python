number = input("Number: ")
g = str(number)
i = 0
list = []
while i < len(g):
    list.append(int(g[i]))
    i += 1

def arithmetic_sequence(list):
    if len(list) == 2:
        "Need more than 2 numbers"
    if list[1] < list[0]:
        a = abs(list[0] - list[1])
    else:
        a = abs(list[1] - list[0])

    for i in range(len(list) - 1):
        if abs(list[i + 1] - list[i]) != a:
            return "It is not a arithmetic sequence"

    return "It is a arithmetic sequence"

print arithmetic_sequence(list)


