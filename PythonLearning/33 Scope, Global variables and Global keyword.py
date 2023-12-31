
l = 10   # Global variable.
def function1(n):
    # l = 5   # Local variable.
    # l = l+45 # throw error, you cannot change global variables.
    # To change global variables you have to use global keyword:
    global l
    l = l+45        # value of global variable changed to 55.
    print(l)
    print(n, "I have printed.")

function1("This is me")
print(l)


def harry():
    x = 20
    def rohan():
    # global keyword checks global variable outside the all function. This means rohan() will not change value of x inside harry() as it not a global variable:
        global x
        x = 88
    print("Before calling rohan()",x) #20
    rohan()
    print("After calling rohan()",x)    #20

harry()