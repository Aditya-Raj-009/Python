class Employee:
    number_of_leaaves = 8 # class variable (this can be use by harry and rohan both and those who are object of this class)
    pass

harry = Employee()
rohan = Employee()
# Instance variables:
harry.name = "Harry"
harry.salary = 55000
harry.role = "Coder"
print(harry.name, harry.salary,harry.role)
print(harry.number_of_leaaves)
print(Employee.number_of_leaaves)   # also called by class name.

rohan.name = "Rohan"
rohan.salary = "700000"
rohan.role = "Engineer"
print(rohan.name, rohan.salary,rohan.role)
print(rohan.number_of_leaaves)

# you can change the value of class variable by instance of the class. but this change for that object only.
# But if you want to do change for all then change by class name:
Employee.number_of_leaaves = 20
# changes for both:
print(harry.number_of_leaaves)
print(rohan.number_of_leaaves)

# if u try to change by instance , it will only change for rohan:
rohan.number_of_leaaves = 3;
print(rohan.number_of_leaaves)

# to verify this , we have a attribute __dict__ this attribute is defined in all classes:
# this return a dictionary of all instance variables which are created:
print(rohan.__dict__)
print(harry.__dict__)

# you can delete properties on object bu using the del keyword:
del harry.number_of_leaaves
# print(harry.number_of_leaaves)  # throw error.