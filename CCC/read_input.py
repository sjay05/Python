"""
4
1
2
3
4
"""

def read_input(func):
    all_input = []
    number_of_lines = input()
    while number_of_lines > 0:
        line = raw_input().rstrip()
        all_input.append(func(line))
        number_of_lines -= 1

    return all_input

def flatten(list):
    flat = []
    for i in list:
        flat.extend(i)
    return flat

str_to_int = lambda i: [int(x) for x in i.split(" ")]


#print read_input(lambda i: int(i))
#i = read_input(lambda i: [int(x) for x in i.split(" ")])
#print flatten(i)
#print read_input(lambda i: str(i))





