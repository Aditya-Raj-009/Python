# Let understand raise by examples:

a = input("What is your name?")
b = int(input("How much do you earn?"))
if b == 0:
    raise ZeroDivisionError('since b is 0 we stopping programe...')

if a.isnumeric():
    raise Exception("Numbers are not allowed")      # here raise is similar to throw keyword in java.

print("Hello")


c = input("Enter your name: ")
try:
    print(k)

except Exception as e:
    print(e)
    if c=="prince":
        raise ValueError("prince is not allowed")
    print("Exception is handled")