def function1():
    print("subscribe now!")


# If I do this:
func2 = function1
# Then I can do this:
func2()  # it work as function1 becoz func2 is a copy of function1

# even if i delete the function1 ,func2 will not get effected:
del function1  # deleted.
func2()  # still work as function1


# function returns function:

def funret(num):
    if num == 0:
        return print  # print is a function.
    if num == 1:
        return int  # int is a function.


a = funret(1)
print(a)  # <class 'int'>
# since a is now int , we can use b as int:
k = "2"
result = a(k) + 1
print(result)

b = funret(0)
print(b)  # <built-in function print>
# since b is now print function, we can use b as print() function:
b("hello")


# function takes argument as function:

def executer(func):
    func("helloWorld")  # whatever function will comes as argument, will called here.


executer(print)  # passing print function as parameter

# Now we talk about decorator:
print("\nNow all about decorator:\n")


def dec1(func1):
    def nowExecute():
        print("executing now!")
        func1()
        print("Func1 executed")

    return nowExecute


def whoisi():
    print("I am a good boy")


# whoisi() # I am a good boy
# but if i do :
# whoisi = dec1(whoisi)   # now whoisi act as whatever dec1 returns..ie. nowExecute()
#
# whoisi()    # now whoisi act as nowExecute()

# now instead of doing above we can also do the same thing by using @ above whoisi():
@dec1
def whoisi():
    print("I am a good boy")


whoisi()
