# Function that reverses the order of the words in a string.
string = "Do or do not, there is no try"

def reverse_str(words):
    list_words = words.split(' ')
    i = len(list_words)-1
    final = []
    while i >= 0:
        final.append(list_words[i])
        i -= 1

    print final

reverse_str(string)