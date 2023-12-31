import math

# F Strings:

me = "Aditya"
a1 = 5

# string formatting:

# way 1:
# a = "this is %s" % me
# way 2:
# a =  "this is %s %s" % (me,a1)
# way 3:
# a = "this is {1} {0}"      # by default index in {} {} is 0 and 1.
# b = a.format(me,a1) # according to index in {} {} will fit.
# print(b)

# way 4 using f-strings :
# a = f"this is {me} {a1}"
# a = f"this is {me} {a1} {4*3}"
a = f"this is {me} {a1} {math.cos(45)}"
print(a)
