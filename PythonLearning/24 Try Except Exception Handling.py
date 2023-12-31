
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
# This can throw exception if num2 =  0. to handle exception we put this under try-except:
try:
    print("The quotient is",        # you can press enter after comma in print statement.
          num1/num2)
except Exception as e:              # catch exception.
    print(e)

print("This line is very important.")