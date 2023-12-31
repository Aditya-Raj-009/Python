class Employee2:
    no_of_leaves = 8

    # method which start and end with underscore-underscore is called Dunder method.
    # constructor is a dunder method.

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

    # dunder method(inbuilt): this helps in operator overloading:
    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary // other.salary

    # for more dunder method please check out for Mapping Operators to functions...documentation.

    # now we talk about repr and str (inbuilt methods):

    # repr helps in printing details of a object when we prints object of a class:
    def __repr__(self):
        return f"Employee2('{self.name}',{self.salary},'{self.roll}')"

    #     str:
    def __str__(self):
        return self.printdetails()


emp1 = Employee2("Prince", 332367783, "Programmer")
emp2 = Employee2("Rohan", 3343, "Cleaner")
print(emp1 + emp2)  # if dunder method were not there then it shows error.
print(emp1 / emp2)

# print(emp1)  # <__main__.Employee2 object at 0x00000262C0627D90>

# after repr method:
# print(emp1)  # Employee2('Prince',332367783,'Programmer')

# after str method:
# it first prefer to run str if present otherwise repr method:
print(emp1)  # Name is Prince, salary is 332367783 and roll is Programmer.

# if we want to print a particular method (str or repr):
print(repr(emp1))
print(str(emp1))

