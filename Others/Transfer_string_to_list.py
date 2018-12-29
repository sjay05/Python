name = "Sanjay"

def transfer_string_to_list(name):
    i = 0
    list = []
    while i < len(name):
        list.append(name[i])
        i += 1
    return list

print transfer_string_to_list(name)


