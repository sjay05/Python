input_list = [5, 6, 7, 8, 9, 10]
number_of_rotation = 4
new_list = []

for i in range(number_of_rotation):
    new_list.append(input_list[i])

if number_of_rotation == len(input_list):
    print input_list
else:
    for a in range(len(new_list)):
        input_list.remove(new_list[a])

    for p in range(len(new_list)):
        input_list.append(new_list[p])

    print input_list
