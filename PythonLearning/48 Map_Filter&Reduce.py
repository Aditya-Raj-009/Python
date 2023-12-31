number = ["3","4","5"]
# number[2] = number[2]+1 # if i run it, throw an error because list is in string and i am adding integer to the string.

# so if i want to typecast all the elements present in the list into the integer, i might use for loop:
# for i in range(len (number)):
#     number[i] = int(number[i])
#
# number[2] = number[2]+1 # now it will not throw error.
# print(number)

# but this process of typecasting through for loop takes multi lines.
# so we use map(function,iterable)
# map() will convert all the items in the list to integer. also we have to typecast to list. because map function return object.

number = list(map(int,number))
number[2] = number[2]+1
print(number)

# map(function,list): type in the map can be any things for example it can be your own also:

myList = [2,3,4,5,6]
# def sq(a):
#     return a*a
#
# myList = list(map(sq,myList)) # type is square
#
# print(myList)

# above proble by lambda function:

myList = list(map(lambda a:a*a,myList))
print(myList)

def  square(a):
    return a*a

def cube(a):
    return a*a*a

function = [square,cube]
for i in range(5):
    val = list(map(lambda x: x(i),function))
    print(val)

# Filter() function is used to generate an output list of values that return true when the function is called:
# filter(function,iterables):

list_1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

gr_than_5 = list(filter(is_greater_5,list_1))
print(gr_than_5)


# reduce() function is a function of functools module:
from functools import reduce

list_2 = [1,2,3,4]
# suppose u want to do sum of list.then you use for loop to do this:
sum = 0
for i in list_2:
    sum+=i
print(f"using for loop {sum}")

# But u can do this in more easy way by using reduce():
num = reduce(lambda x,y: x+y,list_2)
print(f"using reduce funtion {num}")