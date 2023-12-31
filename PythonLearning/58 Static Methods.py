class Employee2:
    no_of_leaves = 8    # class variable.

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
    def from_str(cls,string):
        return cls(*string.split("-"))

#     To create static methods we use @staticmethod decorator.
#     static method is just a simple method which doesn't take "self" as argument. It means this method cannot
# modify object properties.
#     There are two way to create static method :
#         1) using staticmethod() at call time.
#         2) using @staticmethod at the time of creation of method.(Best way)

    def addNumber(n1,n2):
        return n1+n2

    @staticmethod
    def subtractNumber(n1,n2):
        return n1-n2



harry = Employee2("Harry", 448789, "Instructor")
rohan = Employee2("Rohan", 5690867, "Student")

karan = Employee2.from_str("Karan-33432-designer")
print(karan.salary)
print(karan.no_of_leaves)

# print(karan.addNumber(2,3)) # show error at the time of Output, becoz there is not mention that this method is static or not.
#  to solve this we staticmethod():
karan.addNumber = staticmethod(Employee2.addNumber)
print(karan.addNumber(2,4))
# but this way is not good to use and also good to create static method. Hence we @staticmethod approach:
print(karan.subtractNumber(4,6))