class Employee2:
    no_of_leaves = 8
    var = 8

    def __init__(self, name, salary, roll):
        self.name = name
        self.salary = salary
        self.roll = roll

    def printdetails(self):
        return f"Name is {self.name}, salary is {self.salary} and roll is {self.roll}."

    @classmethod
    def change(cls, newleaves):
        cls.no_of_leaves = newleaves
        cls.newvariable = 20

    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def subtractNumber(n1, n2):
        return n1 - n2


class player:
    noofgame = 4
    var = 9

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printDetails(self):
        return f"The name is {self.name},game is {self.game}"


#     Multiple inheritance:
class coolProgrammer(Employee2,
                     player):  # Order matter,becoz child class first check for data in it own class then in Employee and last in player class.
    language = "C++"
    var = 10

    def printLanguage(self):
        print(f"{self.language}")


harry = Employee2("Harry", 448789, "Instructor")
rohan = Employee2("Rohan", 5690867, "Student")
print(harry.printdetails())
print(harry.printdetails())

shubham = player("Shubham", ["Tennis", "volleyball", "chess", "Ludo", "Football"])

# As coolProgrammer() first inherit Employee2 class, it throw error if we make object without passing arguments of Employee class.
# karan = coolProgrammer()    # TypeError: Employee2.__init__() missing 3 required positional arguments: 'name', 'salary', and 'roll'
karan = coolProgrammer("Karan", 3455, "coolProgrammer")  # passing name,salary,roll.
print(
    karan.printdetails())  # first search in Employee class.If we try to run method of player class , it throw error becoz we haven't pass argument of player class.
karan.printLanguage()
# first search in its own class then in Employee and last in player:
print(karan.var)  # print var of coolProgrammer class.
