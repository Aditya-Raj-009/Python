# pickle module = As you know everything in python is a object. so pickle is use to store python objects:

import pickle

# pickling a python object (list) :

# cars = ["Audi","BMW","Maruti Suzuki","Haryti Tuzuki"]
#
# file = "myCar.pkl"  # need to store pickle.
#
# fileObj = open(file,'wb')    # pickl are in binary.
#
# # dump() function in pickle module use to convert in pickle:
# pickle.dump(cars,fileObj)   # dump take object and fileObject as argument.
# fileObj.close()

# depickling (upack):

file = "myCar.pkl"
with open(file,"rb") as fileObj:    # opening as read binary mode.
    mycar = pickle.load(fileObj)    # use convert in original format (python format).
    print(mycar)
print(type(mycar))  # object introspection