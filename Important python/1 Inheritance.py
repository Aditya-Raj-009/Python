class Father:  # Base class
    def __init__(self, fname, lname):
        self.firstname = fname  # here self.firstname and self.lastname is instance variables.
        self.lastname = lname

    def printname(self):
        print(f"Father's name is {self.firstname} {self.lastname}.")


# x = Father("Rahul", "Tripathy")
# x.printname()


class Son(Father):  # derived class.

    # after adding constructor of son class, son will no longer inherit the father's class.
    # Actually this will override father's class constructor:

    def __init__(self, fname, lname, year):

        # to keep the inheritance of parent's __init__() function, add a call to the parent's __init__() function:

        # Father.__init__(self, fname, lname)

        # instead of using name of the parent element, we use super() keyword . it will automatically inherit
        # the method and properties from its parent.

        super().__init__(fname, lname)  # when we call from super() we don't have to put self.

        self.graduationyear = year

    def welecome(self):
        print(f"welcome {self.firstname} {self.lastname}")


y = Son("Mahesh", "Tripathy", 2025)
y.printname()   # call parent class method.
y.welecome()    # call derived class method.