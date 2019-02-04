"""Converting Decimal Numbers to Binary Numbers Using Stacks"""


# The divide by 2 algorithm starts with a integer greater than 0. A simple iteration
# continues to divide the decimal number by 2 and keeps track of the remainder. Every
# remainder is pushed into a stack and when the quotient equals 0, all of the contents
# are pushed out into a string/list.


""" REPRESENTATION WHEN GIVEN INTEGER 223

        223 //2 = 116 (rem = 1)
        
            116 // 2 = 58 (rem = 0) 
            
                58 // 2 = 29 (rem = 0)
                
                    29 // 2 = 14 (rem = 1)
                     
                        14 // 2 = 7 (rem = 0) 
                        
                            7 / 2 = 3 (rem = 1)
                             
                                3 // 2 = 1 (rem = 1)
                                
                                    1 // 2 = 0  (rem = 1) ***STOP HERE***
                    
            pop remainders
       <------------------------
Stack: [1, 0, 0, 1, 0 , 1, 1, 1]     --->    BINARY REP. OF 223 = 10010111 
        ------------------------> 
            push remainders 

"""


# OOP Implementation of all STACK


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# Code for converting Decimal to Binary using Stack OOP
def divide_by2(dec_number):
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number = dec_number // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string


print(divide_by2(input("Number to be converted into Binary Rep.: ")))
