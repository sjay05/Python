from CCC.read_input import *

n = 4
rounds = flatten(read_input(str_to_int))
antonia = 100
david = 100
i = 0

while i <= len(rounds) - 2:
    if rounds[i] < rounds[i+1]:
        antonia = antonia - rounds[i+1]
        i += 2
    elif rounds[i] > rounds[i+1]:
        david = david - rounds[i]
        i += 2
    elif rounds[i] == rounds[i+1]:
        i += 2

print antonia
print david

