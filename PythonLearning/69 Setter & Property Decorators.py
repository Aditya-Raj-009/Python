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
print(hindu.explain())
print(lover.explain())
print(hindu.Email)  # when we use getter property (@property decorator) we doesn't need to put call means "()" for calling a method
print(lover.Email)

# if u want to change your name (instance variable):

# change because we comment out email from constructor.
# If we not do so,it will not change since it is inside constructor it will call at the creation of object:
hindu.fname = "Rajputana"
print(hindu.Email)  # Rajputana.Raj@codeWithPrince.com

hindu.Email = "AdiManouv.Raj@CodeWithPrince.com"    # if we do without setter property , it will show error.
print(hindu.Email)  # Changed
print(hindu.fname)  # AdiManouv (changed fname).

del hindu.Email  # if we do without deleter decorator , it will throw error.

print(hindu.Email)  # Email is not set! : output.
print(hindu.fname)  # None
print(hindu.lname)  # None

# we cannot use setter decorator without getter (@property) decorator.
