data = []
while True:
    line = raw_input()
    if line == "0":
        break
    else:
        iline = [int(x) for x in line.split(" ")]
        data.append(iline)

for i in range(len(data)):
    focus = data[i]
    diff = []
    focus.remove(focus[0])

    for a in range(len(focus)-1):
        diff.append(focus[a+1] - focus[a])

    final = []
    for p in range(len(diff)):
        if diff[p] not in final:
            final.append(diff[p])
        else:
