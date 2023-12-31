a = 9
b = 13
c = sum((a, b))  # sum() is a inbuilt method in python. you have pass number in list or in tuple form.
print(c)  # 22


# creating own function (User defined function) :
''' def keyword is use to create function.
'''
def MyFunc1():
    print("Hello you are in MyFunction1.")

# calling MyFunction1():
print(MyFunc1())  # Hello you are in MyFunction1.
# None, print None because function is returning nothing.

# this time none will not print:
MyFunc1()  # Hello you are in MyFunction1.



# function taking input:
def MyFuction2(a, b):
    print(a+b)

# Calling function:
MyFuction2(3,5) # 8



# finding average of two numbers:
def MyFunction3(a,b):
    # docs_string: Anything written as multi-line comment in the first line of the function is called docs string:
    '''This is a void type function which calculate average of two number.'''
    average = (a+b)/2
    print(average)

# Calling function:
MyFunction3(45,65)
v = MyFunction3(45,76)
print(v)    # None, because return nothing.


# funtion returning:
def average(a,b):
    '''This is a integer return type function which calculate average of two number.'''  # docs_string.
    return (a+b)/2

#Calling function:
k = average(34,67)
print(k)    # 50.5


#  to read docs string of any functions:
print(average.__doc__)  # This is a integer return type function which calculate average of two number.
print(MyFunction3.__doc__)  # This is a void type function which calculate average of two number.