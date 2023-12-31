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

    # we are using a method as alternative constructor:
    @classmethod
    def from_str(cls,string):
        # params = string.split("-")
        # return cls(params[0],params[1],params[2])  # creating and returning a object.

#         Know we use *args for above operation to make it short:
        return cls(*string.split("-")) # pass all data as argument.


harry = Employee2("Harry", 448789, "Instructor")
rohan = Employee2("Rohan", 5690867, "Student")
# here we use class method to create object for karan. Just by passing all data in a single string:
karan = Employee2.from_str("Karan-33432-designer")
print(karan.salary)
print(karan.no_of_leaves)