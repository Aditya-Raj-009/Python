class Employee2:
    no_of_leaves = 8

    def __init__(self, name, salary, roll):
        # setting instance variables:
        self.name = name
        self.salary = salary
        self.roll = roll

    def printdetails(self):  # 'self' keyword is same as 'this' in java , it refer to the current object. you can write anything instead of 'self'.
        return f"Name is {self.name}, salary is {self.salary} and roll is {self.roll}."


harry = Employee2("Harry", 448789, "Instructor")
rohan = Employee2("Rohan", 5690867, "Student")

# harry.name = "Harry"
# harry.salary = 440000
# harry.roll = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 640000
# rohan.roll = "Student"

print(rohan.printdetails())  # here on calling by rohan , it automatically take "rohan" as "self" argument.
print(harry.printdetails())  # here on calling by harry , it automatically take "harry" as "self" argument.
print(harry.salary)
