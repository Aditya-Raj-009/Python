# opening file:

# f = open("prince.txt","r")  # r is a by default mode. output will not change even if u not mention "r".
# f = open("prince.txt","rt") # rt (read in text mode)  is a by default mode. output will not change even if u not mention "rt".

f = open("prince.txt")

# read() - to read a file:

'''
# content = f.read() # read whole content.
# content = f.read(3) # read only 3 characters.

print(content) # whatever content in file will print.


#  reading file using for loop:

# for line in f:
#     print(line,end="")


# print(f.readline())     # read a single line only.

# print(f.readlines())  # all content will print as a list.

'''


f.close() # a good practice to close a file after reading or writing.

