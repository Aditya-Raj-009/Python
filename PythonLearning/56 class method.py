class Employee2:
    no_of_leaves = 8    # class variable.

    def __init__(self, name, salary, roll):
        # setting instance variables:
        self.name = name
        self.salary = salary
        self.roll = roll

    def printdetails(self):  # 'self' keyword is same as 'this' in java , it refer to the current object. you can write anything instead of 'self'.
        return f"Name is {self.name}, salary is {self.salary} and roll is {self.roll}."

#     creating class method:
    @classmethod    # this is a class method decorator.
    def change(cls, newleaves):     # here cls is for class. jaise self instance ke liye hota h.
        cls.no_of_leaves = newleaves
        # we can also create class variable:
        cls.newvariable = 20


harry = Employee2("Harry", 448789, "Instructor")
rohan = Employee2("Rohan", 5690867, "Student")

print(harry.no_of_leaves)
# as we know , we cannot change the value of class variable using instance of the class.
# so to change this we use class name :
# Employee2.no_of_leaves = 12

# But there is another way to change class variable, that is by creating class method:
harry.change(45)
# change for both:
print(harry.no_of_leaves)
print(rohan.no_of_leaves)

print(harry.newvariable)
print(rohan.newvariable)