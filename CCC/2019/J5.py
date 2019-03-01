rule1 = raw_input()
rule1 = rule1.rsplit()
rule2 = raw_input()
rule2 = rule2.rsplit()
rule3 = raw_input()
rule3 = rule3.rsplit()
final = raw_input()
final = final.rsplit()

starts = []
starts.append(rule1[0])
starts.append(rule2[0])
starts.append(rule3[0])

while True:
    beginning = final[1]
    if beginning in starts:


