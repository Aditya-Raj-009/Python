var1 = 6
var2 = 56

var3 = int(input())
'''
logical operator in python:
and : same work as && do in java.
or : same work as || do in java.
not : same work as ! do in java.
'''

if var3>var2 and var3<100:
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("Lesser")

list = [4,6,3,7]

# in and not is a keyword in python :

# check if that element is present in the list or not. If present return true otherwise false:
print(6 in list)
if 6 in list:
        print("Yes its in the list")

# check if that element is present in the list or not. If not present return true otherwise false:
print(10 not in list)
if 10 not in list:
    print("Yes it is not present in list")