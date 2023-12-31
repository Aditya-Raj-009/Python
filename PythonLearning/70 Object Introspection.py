class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codeWithPrince.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    #  Getter in python:
    @property  # ADV. by this we doesn't need to use '()' for calling any method.
    def Email(self):
        if self.fname is None or self.lname is None:
            return "Email is not set!"

        return f"{self.fname}.{self.lname}@codeWithPrince.com"

    # Now if we want to set or change Email Attribute. We use setter attribute :

    @Email.setter  # way of using setter decorator: @changeForWhichWeWant.setter
    def Email(self, string):
        print("changing email Attribute...")
        name = string.split("@")[0]  # to access first element.
        self.fname = name.split(".")[0]  # to access first element.
        self.lname = name.split(".")[1]

    #     do delete attribute: There is a deleter decorator:

    @Email.deleter
    def Email(self):
        self.fname = None
        self.lname = None


hindu = Employee("Aditya", "Raj")
lover = Employee("Love", "Singh")

# In python Object Introspection means to get information about any Objects:

# to get class of any object:
print(type(hindu))

# to get id:
print(id(hindu))
print(id(lover))

# to get attribute define for this object:
print(dir(hindu))

# to get attribute define for this object:

import inspect

print(inspect.getmembers(hindu))
