# If u do not know how many arguments that will be passed into your function then we simply use the two way:
#  *args and **Kwargs.

# *args use to take a tuple of arguments and can access the items accordingly:
# example 1:
def myFunction(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

print(myFunction(2,3,4,5,6,7))

# example 2:
def printMyname(*kids):
    print(kids[2])

printMyname("Rahul","jenny","aryan","Aditya")

# **Kwargs is a Arbitary keyword arguments, this take arguments as dictionary inside the function.
# example 1:
def myFunc(**kids):
    print(kids["lname"])

myFunc(fname= "Aditya",lname= "Raj")

# example 2:
def intro(**data):
    for key,val in data.items():
        print("{} is {}".format(key,val))

intro(Name="Aditya Raj",Email= "princeSinghRajput08679@gmail.com",mobile_no= 9693494500,country="India",age=19)

# default parameter value:
def urId(defaultId = "192939@97"):
    print(f"Your default id is {defaultId}")

urId()

# Pass statement:
# function definition cannot be empty, but if you for some reason have a function defition with no content, put
# in the pass statement to avoid getting an error.
def empty():
    pass

empty()