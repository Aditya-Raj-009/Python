ls = []
for i in range(50):
    if i % 3 == 0:
        ls.append(i)

print(ls)

# But above work can be done by a short way by using list comprehension:
# List comprehension: This is a short cut way to create a list:

nls = [i for i in range(20) if i % 3 == 0]
print(nls)


# Dictionary comprehension: This is a short cut way to create a dictionary:

# di = {i: f"item {i}" for i in range(100) if i % 10 == 0}
# print(di)

di = {i: f"Item {i}" for i in range(5)}
print(di)

#  we can also use dictionary comprehension for reversing key-value pair:

dict1 = {value: key for key, value in di.items()}
print(dict1)


# set comprehension:

dresses = {dress for dress in ["dress1","dress1","dress1","dress1","dress1","dress1","dress1"]}
print(dresses)  # since set is a collection of unique element. output will only : {'dress1'}

set1 = {i for i in range(10)}
print(set1)


# generator comprehension:

even = (i for i in range(100) if i % 2 ==0)
print(type(even))   # <class 'generator'>

print(even.__next__())
print(even.__next__())
print(even.__next__())
print(even.__next__())
for i in even:
    print(i)

