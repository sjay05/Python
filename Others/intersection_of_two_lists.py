list1 = [2, 3, 4, 5, 8]
list2 = [2, 3, 5, 7, 8, 9]
new_list = []

def intersect(new_list, list1, list2):
    for i in range(0, len(list1)):
        if list1[i] in list2:
            new_list.append(list1[i])
        i += 1

if len(list1) < len(list2):
    intersect(new_list, list1, list2)
else:
    intersect(new_list, list2, list1)


print new_list

