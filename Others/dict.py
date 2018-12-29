input = "seeni"

# Dictionary or Hashtable
output = {}

for c in input:
    count = output.get(c, 0)
    count += 1
    output.update({c: count})

print output




