# Python Object-Oriented Programming for an employee

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)




emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)



#This is the bad way of giving in the information
#emp_1.first = 'Corey'
#emp_1.last = 'Schafer'
#emp_1.email = 'Corey.Schafer@company.com'
#emp_1.pay = 50000


#emp_2.first = 'Test'
#emp_2.last = 'User'
#emp_2.email = 'Test.User@company.com'
#emp_2.pay = 60000


print emp_1.email
print emp_2.email

print emp_1.fullname()
print emp_2.fullname()

#Printing the fullname using the class instead of the function
print emp_1.fullname()
print Employee.fullname(emp_1)




