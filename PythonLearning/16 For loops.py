list = ["Harry","Prince","Aditya","Carry Minati"]

# creating for loop:
# using this, for loop will iterate in list and print all the items :
for i in list:
    print(i)

# use of for loop for list in list:
list2 = [ ["Harry",4],["Prince",8],["Aditya",3],["Carry Minati",7] ]
for i in list2:
    print(i)  # ['Harry', 4] ['Prince', 8] ['Aditya', 3]

for i, j in list2:
    print(i, j)     # Harry 4 Prince 8 Aditya 3 Carry Minati 7

# typecasting of list into dictionary:

# dict() keyword use for typecasting into dictionary:
Mydict = dict(list2)
print(Mydict)  # {'Harry': 4, 'Prince': 8, 'Aditya': 3, 'Carry Minati': 7}

# for loop use in dictionary:
for i in Mydict:
    print(i) # only keys will print.

for i, j in Mydict.items():
    print(i,j) # Harry 4 Prince 8 Aditya 3 Carry Minati 7
