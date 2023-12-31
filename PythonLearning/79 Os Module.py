import os   # os stands for operating system.

# print(dir(os))  # print a list of method present in this module.

# print(os.getcwd())  # to get current working directory. (output: D:\Python\PythonLearning)

#  To change current working directory:
# os.chdir("C://")    # move to C
# to verify to change in directory:
# print(os.getcwd())  # changed to C  (output: C:\)

# print(os.listdir())     # print a list of all folder and file present in current directory (C).
# print(os.listdir("C://"))    # print a list of all folder and file present in a given path.

# To make folder:
# first we have change our directory so that we can create for folder here:
# os.chdir("D:/Python/PythonLearning")
# # to verify to change in directory:
print(os.getcwd())

# Now create folder using function - mkdir():
# os.mkdir("Folder created using python") # folder created.

#  to make multiple directory at a time we use makedirs():
# os.makedirs("This/That")    # create a folder This and inside this That folder will created.

# Delete or remove folder from directory:
# os.rmdir("Folder created using python") # removed.
# os.rmdir("This/That")     # removed "That"
# os.rmdir("This")    # removed "This"

# To rename a folder or file:
# os.rename("prince.txt","Aditya.txt")    # rename file prince to Aditya.

# To read environment variable:
# print(os.environ.get("Path"))

# to join two path:
# print(os.path.join("D:/","Aditya.txt"))

# to check whether path exist or not:
print(os.path.exists("Aditya.txt"))     # return True, becoz this path exist.

# to check whether it is dir or not:
print(os.path.isdir("Aditya.txt"))     # return False, becoz this a file.

# to check whether it is file or not:
print(os.path.isfile("Aditya.txt"))     # return True, becoz this path exist.
