# Link: https://leetcode.com/problems/count-and-say/
# This is a solution to the Count_And_Say problem.
def translate(number):
    main_break = False
    count = 0
    word = ""
    while True:
        if main_break:
            return word
        elif count == len(number)-1:
            word += "1"
            word += number[count]
            return word
        elif number[count] == number[count+1]:
            var_count = 1
            while True:
                if count == len(number)-1:
                    word += str(var_count)
                    word += number[count]
                    main_break = True
                    break
                elif number[count] != number[count+1]:
                    word += str(var_count)
                    word += number[count]
                    count += 1
                    break
                else:
                    var_count += 1
                    count += 1

        else:
            word += "1"
            word += number[count]
            count += 1

def count_and_say(value):
    word = ""
    for i in range(value-1):
        if i == 0:
            word = translate("1")
        else:
            word = translate(word)

    return word

print count_and_say(9)


