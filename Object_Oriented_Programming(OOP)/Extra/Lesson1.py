#The program below has to do everything about an object called pet.

class pet:
    #defining the number of legs (The first attribute of a pet)
    number_of_legs = 0

    #Sleep function for pet
    def sleep(self):
        print "zzz"

    #Count_legs function to state the number of legs the pet has
    def count_legs(self):
        print "I have %s legs" % self.number_of_legs

#Writing pet's name as doug and referring to the class
doug = pet()
#Initiallizing the number of legs
doug.number_of_legs = 4
#asking to print the function "Count_legs"
doug.count_legs()

#Example for another pet called nemo that resembles a fish
nemo = pet()
nemo.number_of_legs = 0
nemo.count_legs()