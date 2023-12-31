class Employee2:
    # to make public just keep as it is:
    no_of_leaves = 8    # public
    var = 8     # public

    # to keep protected, start naming by underscore:
    _city = "Mumbai"    # Protected.

    # to keep privatem, we use double underscore:
    __priv = 900    # Private.

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

emp = Employee2("Aditya",3433,"partime")
print(emp._city)    # access protected data ,class which are inheriting this class can also access.
print(emp._Employee2__priv)     # way of accessing private data.    No one can access this data, even subclass also cannot access it.

