list = [1, 2, 3, 3, 2, 1, 5, 5, 10, 10]
new_list = []
i = 0

while i < len(list):
    if list[i] not in new_list:
        new_list.append(list[i])

    i += 1

print new_list