input = "1001"
i = 0
par = len(input) - 1

def is_palindrome(input):
    i = 0
    par = len(input) - 1
    while i < par:
        if input[i] != input[par]:
            return False
        i += 1
        par -= 1

    return True

if is_palindrome(input):
    print "It is a palindrome"
else:
    print "It is not a palindrome"




