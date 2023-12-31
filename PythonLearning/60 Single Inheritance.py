class Employee2:
    no_of_leaves = 8

    def __init__(self, name, salary, roll):
        self.name = name
        self.salary = salary
        self.roll = roll

    def printdetails(self):
        return f"Name is {self.name}, salary is {self.salary} and roll is {self.roll}."

    @classmethod
    def change(cls, newleaves):
        cls.no_of_leaves = newleaves
        cls.newvariable = 20

    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def subtractNumber(n1, n2):
        return n1 - n2


class Programmer(Employee2):    # inheriting Employee2 class.
    def __init__(self, name, salary, roll,languages):
        # Employee2.__init__(self,name,salary,roll)   # calling parent's constructor by its class name.

# we can also call it by super() keyword. here super() is same as java.But one more befit here is we
        # don't need to pass self as argument when we use super():

#         super().__init__(name,salary,roll)

#         OR we can also pass two parameter in super(subclass name,self) :

        super(Programmer, self).__init__(name,salary,roll)

        self.languages = languages

    def printprog(self):
        return f"Name is {self.name}, salary is {self.salary} , roll is {self.roll} and languages is {self.languages}."


harry = Employee2("Harry", 448789, "Instructor")
rohan = Employee2("Rohan", 5690867, "Student")
print(harry.printdetails())
print(harry.printdetails())

shubham = Programmer("Shubham", 56645443, "Programmer",["Java","Python","C","JavaScript"])
karan = Programmer("Karan", 35464243, "Programmer",["Java","Python","C","JavaScript"])
print(shubham.printprog())
print(karan.printprog())
# can also access employee2's member:
print(shubham.printdetails())
print(karan.printdetails())
