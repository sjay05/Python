class pet:
    number_of_legs = 0

    def sleep(self):
        print "zzz"

    def count_legs(self):
        print "I have %s legs" % self.number_of_legs

#Now a new class and in the brackets we write the inheriting class
class dog(pet):
    def bark(self):
        print "woof"

doug = dog()
doug.sleep()
doug.number_of_legs = 4
doug.count_legs()