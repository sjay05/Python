n = raw_input()
brackets = []

brackets_pair = {")": "(", "}": "{", "]": "["}


def bracket_sorter(b):
    if b in brackets_pair.values():
        brackets.append(b)
    elif len(brackets) and brackets_pair[b] != brackets.pop():
        return False
    return True


for i in range(len(n)):
    if not bracket_sorter(n[i]):
        break

if len(brackets) == 0:
    print "True"
else:
    print "False"



