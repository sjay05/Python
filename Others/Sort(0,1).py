list = [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
pointer1 = 0
pointer2 = 1

def swap(a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = tempz

while pointer2 <= len(list)-1:

    if list[pointer1] < list[pointer2] or list[pointer1] == 0 and list[pointer2] == 0 :
        pointer1 += 1
        pointer2 += 1

    elif list[pointer1] > list[pointer2]:
        swap(pointer1, pointer2)
        pointer1 += 1
        pointer2 += 1

    elif list[pointer1] == 1 and list[pointer2] == 1 and pointer2 < (len(list)-1):
        pointer2 += 1

        while list[pointer2] == 1 and pointer2 <= len(list)-1:
            pointer2 += 1
            
        if list[pointer1] > list[pointer2]:
            swap(pointer1, pointer2)

        if pointer2 == len(list)-1:
            break
        else:
            pointer1 += 1

print list


























