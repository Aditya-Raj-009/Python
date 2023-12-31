class A:
    classVar1 = "I am in class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classVar1 = "Instance variable in class A"
        self.special = "I am special in class A"


class B(A):
    classVar2 = "I am in class variable in class B"

    # override:
    classVar1 = "I am in class variable in class B (Override)"

    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's constructor"
        print(super().classVar1)
        # self.classVar1 = "I am instance variable in class B"


a = A()
b = B()

# first find Instance variable in its own class, If not found then find in parent class.
# And if variable is not found in instance variable then it check for class variable one by one (first in its own class then in parent class):
print(b.classVar1)
print(b.special)
