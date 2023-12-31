# Operators in python:
'''
1. Arithmetics Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
'''

# Arithmetics Operators:
print("5+6 is", 5 + 6)
print("5-6 is", 5 - 6)
print("5*6 is", 5 * 6)
print("15/6 in float is", 15 / 6)  # return quotient in float. 2.5 as output.
print("15//6 in integer is", 15 // 6)  # // means return quotient in integer. 2 as output.
print("5%6 is", 5 % 6)
print("5 to power 2 is", 5 ** 2)  # ** use for raise power.

# Assignment Operators:
a = 5
print(a)
a += 7
print(a)
a /= a
print(a)
a -= a
print(a)
a *= a
print(a)

# Comparison Operators:
i = 5
print(i == 5)  # true
print(i != 5)  # false
print(i > 5)  # false
print(i >= 5)  # true

# Logical Operators:
a = True
b = False
print(a and b)  # False
print(a and a)  # True
print(b and b)  # False
print(a or b)  # True

# Identity Operators:
print(a is b)  # False
print(a is not b)  # True
print(5 is not 7)  # True
print(5 is 5)  # True

# Membership Operators:
list = [3, 5, 6, 7, 2, 75, 73, 25, 66, 96]
print(25 in list) # True , because 25 is present in list.
print(25 not in list) # False, because 25 is in list.

# Bitwise Operators:
print(0 | 1)    # 1
print(0 & 1)    # 0
print(2 | 3)    # 3
print(2 & 3)    # 2
