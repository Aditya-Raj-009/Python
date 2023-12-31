# In python if we want abstract class and abstract method we have to import inbuilt module , "abc":

#  if we are using below python 3.4 then import like this:
# from abc import ABCMeta, abstractmethod         # abstractmethod is a decorator in python.

# but for above 3.4 or 3.4 version you have to do just:
from abc import ABC, abstractmethod


class shape(ABC):  # if u are using blow 3.4 then put (metaclass=ABCMeta) in class argument. Otherwise use just (ABC).
    @abstractmethod
    def printarea(self):
        pass


class rectangle(shape):
    type = "Rectangle"
    side = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth


rect1 = rectangle()
print(rect1.printarea())
