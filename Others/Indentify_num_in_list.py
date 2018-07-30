# Write a function to take a number to say whether the number is in the list or not.

num = 5
a = [1, 4, 2, 3]
i = 0 
find = False 


# Second way of solving 
def num_in_list_or_not(num, a):
    i = 0 
    while i < len(a):
        if a[i] == num:
            find = True
            break
    
        i += 1

    if find:
        return "Found the num in the list"
    else:
        return "Num is not found in the list"

print num_in_list_or_not(num, a)


