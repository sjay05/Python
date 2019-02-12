# Write a program which removes duplicates from given list.
array = [1, 2, 3, 4, 5, 6, 6, 7, 8, 10, 2, 3, 3 ,3, 11, 100, 100]
new_array = []
i = 0

while i < len(array):
    if array[i] not in new_array:
        new_array.append(array[i])
    i += 1
print new_array
