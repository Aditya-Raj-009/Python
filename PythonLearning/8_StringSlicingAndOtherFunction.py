mystr = "aditya is a good boy"
print(mystr)

# Slicing:

print(mystr[4]) # y
print(mystr[0:4]) # adit

# if u to print the string by skipping one character. mystr[start index : end index : skipping(by default 1)]:
print(mystr[0:5:2]) # aiy
print(mystr[0::2]) # aiy sago o

print(mystr[0:]) # aditya is a good boy
print(mystr[:6]) # aditya
print(mystr[:]) # aditya is a good boy
print(mystr[::]) # aditya is a good boy

# Slicing by negative indices:
"""
0    1   2   3   4   5   6   7  8  9  10  11  12  13  14  15  16  17  18  19
-----------------------------------------------------------------------------
| a | d | i | t | y | a |  | i | s |  | a |  | g | o | o | d |  | b | o | y |
-----------------------------------------------------------------------------
-20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7  -6  -5  -4 -3  -2  -1
"""
print(mystr[-4:]) #  boy
print(mystr[-5:-2]) #d b
print(mystr[15:18]) #d b

# but if u put negative in 3rd column(skipping index) then it first reverse the string then it start skipping:

print(mystr[::-1]) # yob doog a si aytida
print(mystr[::-2]) # ybdo  iatd

# to find length of a string:
print(len(mystr)) # 20

# Some functions of string:
"""
.isalnum() : return true if all the characters are alphanumeric, meaning alphabet letter (a-z) and number (0-9).
example of characters that are not alphanumeric : (space)!#%&? etc.

.isalpha(): return true if all the characters are alphabet letters (a-z).
example of characters that are not alphabet letters : (space)!#%&? etc.

.isnumeric(): return true if all the characters are numeric (0-9).

.islower().
.isupper().
.istitle().
.isspace().
.isidentifier().
.isdigit().
.isdecimal().
.isascii().
.isprintable().

.endswith(string or character).
.startswith(string or character).

.count(string or character) : count the given string or character.
.capitalize() : capitalize the first letter of the string.

.find(string): to find any string in your string. It returns its index wherever that string is present, and
if not present it returns -1.

.lower() : to convert the string in lower case.
.upper() : to convert the string in upper case.

.replace(string which replace, string that take place).
"""
print(mystr.isalnum()) # False
print(mystr.isalpha()) # False
print(mystr.endswith("boy")) # True
print(mystr.startswith("uy")) # False
print(mystr.count("o")) # 3
print(mystr.capitalize()) # Aditya is a good boy
print(mystr.find('is')) # 7
print(mystr.lower()) # aditya is a good boy
print(mystr.upper()) # ADITYA IS A GOOD BOY
print(mystr.replace("is","are")) # aditya are a good boy