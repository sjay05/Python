import random
print "There is a prize inside one of the 3 doors. Your goal is to guess the correct door number to recieve the prize."
resp = "Y"


def find_other_int(a, b):
    if a == b:
        choice = [i for i in range(0, 3) if i != a]
        return random.choice(choice)
    else:
        return 3 - (a + b)


while resp == "Y":
    secret = ['x', 'x', 'x']
    index = random.randint(0,2)

    first_choice = input("Choose a door number(0, 1, 2): ")
    print "We will reveal one of the doors..."

    rev_num = find_other_int(index, first_choice)
    secret[rev_num] = "goat"

    print secret

    choice = raw_input("Do you wish to change your choice?(Y or N): ")

    if choice == "Y" and index == find_other_int(first_choice, rev_num):
        secret[index] = "prize"
        print "Congratulations! You won the prize!"
        print secret
    elif index == first_choice:
        print "Congratulations! You won"
    else:
        print "Sorry, you lost."

    resp = raw_input("Do you wish to play again?(Y or N): ")


