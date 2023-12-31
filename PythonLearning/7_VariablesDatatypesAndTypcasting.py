#variables:

var1 = "54"
var2 = 4
var3 = 36.7
var4 = "Aditya"
var5 = "32"
print(var1)
print(var2)
print(var3)
# type() function returns variable's type:
print(type(var1))
print(type(var2))
print(type(var3))

print(var2+var3)
print(var1+var4)
#print(var2+var1) # throw error as strings cannot be add with any numbers.

print(var1+var5) # not add just concatenate as 5432. But addition can be possible if we typecast it.

    #typacasting:
"""
   str()
   int()
   float()
   """
print(int(var1)+int(var5)) # 86

# In python if u want to print a statement multiple times through print function:
print(10 * "Hello world\n") # Hello world print 10 times.

#but u cannot do this with number it simply get multiply with that number:
print(10 * int(var1)+int(var5)) # 572

# If u want then u should typecast it first into string:
print(10 * str(int(var1)+int(var5))) #print 10 times 86.

# user input:

print("Enter your number")
# whatever user will input will be input as string:
num = input()
print(num,"as a string")

# to solve this we use type casting:
print("Enter a number")
num2 = int(input())
print(num2+34,"as a integer")

# solve a quiz:--> programe to add two number:
print("Enter first number")
num = int(input())
print("Enter second number")
num2 = int(input())
print("Sum of two numbers is",num+num2)


# Important of single quotes , double quotes and triple quotes in python:

name1 = 'Aditya' # In python we can write string in single quotes also.
name2 = "Aditya" # In python we can write string in double quotes also.
name3 = '''Aditya''' # In python we can write string in triple quotes also.
print("name1 : ",name1)
print("name2 : ",name2)
print("name3 : ",name3)

# if we want to print sigle quotes then it should be in double quotes:
a = "Prince's"
print(a) # Prince's

# if we want to print double quotes then it should be in single quotes:
b = 'Ayush"s'
print(b) # Ayush"s

# if we want to print sigle and double both quotes then it should be in triple quotes:
c = '''Aditya"Singh'Rajput'''
print(c) # Aditya"Singh'Rajput