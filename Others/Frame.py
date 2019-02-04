# Print list of words line by line in a frame

list = ["hihdiuhaiuhdiuahwdiuhqwiuhd", "word", "in", "a", "frame"]

n = []

for i in range(len(list)):
    n.append(len(list[i]))

print "*" * (max(n)+4)
for i in range(len(list)):
    if len(list[i]) < max(n):
        print "*", list[i], " " * (max(n)+1-(len(list[i])+2)), "*"
    else:
        print "*", list[i],"*"

print "*" * (max(n)+4)