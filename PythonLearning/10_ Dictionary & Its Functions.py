#  Dictionary :
# dict = {keys : values}.

d1 = {"Harry": "Burger",
      "Rohan": "Fish",
      "Ajay": "Roti"
      }
print(type(d1))
print(d1)

# to access values by keys:

print(d1["Rohan"]) # Fish
print(d1["Ajay"]) # Roti
print(d1["Harry"]) # Burger

# dictionary inside dictionary:
d2 = {"Harry": "Burger",
      "Rohan": "Fish",
      "Ajay": "Roti",
      "Shubham": {"Break-Fast": "Maggie","Lunch": "chicken","Dinner": "Biryani"}
    }

print(d2["Shubham"]) # {'Break-Fast': 'Maggie', 'Lunch': 'chicken', 'Dinner': 'Biryani'}
print(d2["Shubham"]["Lunch"]) # chicken

# add more element to dictionary:

d2["Ankit"] = "Junk Food"
print(d2) # {'Harry': 'Burger', 'Rohan': 'Fish', 'Ajay': 'Roti', 'Shubham': {'Break-Fast': 'Maggie', 'Lunch': 'chicken', 'Dinner': 'Biryani'}, 'Ankit': 'Junk Food'}
print(d2["Ankit"]) # Junk Food

d2[420] = "chor"  # key as number.
print(d2) # {'Harry': 'Burger', 'Rohan': 'Fish', 'Ajay': 'Roti', 'Shubham': {'Break-Fast': 'Maggie', 'Lunch': 'chicken', 'Dinner': 'Biryani'}, 'Ankit': 'Junk Food', 420: 'chor'}

d2["Mobile-No"] = 9693494500  # value as number
print(d2)

#  to delete elements from dictionary:

del d2[420]
del d2["Mobile-No"]
del d2["Ankit"]
print(d2)  # {'Harry': 'Burger', 'Rohan': 'Fish', 'Ajay': 'Roti', 'Shubham': {'Break-Fast': 'Maggie', 'Lunch': 'chicken', 'Dinner': 'Biryani'}}.

# Functions of dictionary:

'''
.copy : return a copy of dictionary.
.get(keys) : return key's value.
.update({keys:values}) : update dictionary by adding keys and its values.
.keys() : return all keys.
.items() : return a list containing a tuple for each key value pair.
.values() : return a list of all the values in the dictionary.
'''
# if u do like this instead of using copy function then changing in d3 also change in d2. Actually by assign d3 = d2 , d3 becomes ponter for d2 :
d3 = d2
del d3["Rohan"] # also delete in d2
print(d2) # {'Harry': 'Burger', 'Ajay': 'Roti', 'Shubham': {'Break-Fast': 'Maggie', 'Lunch': 'chicken', 'Dinner': 'Biryani'}}
# that's why we use copy function:
d3 = d2.copy()
print(d3)

# know changing in d3 will not effect in d2:
del d3["Harry"]
print(d3) # {'Ajay': 'Roti', 'Shubham': {'Break-Fast': 'Maggie', 'Lunch': 'chicken', 'Dinner': 'Biryani'}} deleted from d3
print(d2) # {'Harry': 'Burger', 'Ajay': 'Roti', 'Shubham': {'Break-Fast': 'Maggie', 'Lunch': 'chicken', 'Dinner': 'Biryani'}} not delete from d2

print(d2.get("Ajay")) # Roti

d2.update({"Leena":"Toffee"})
print(d2) # {'Harry': 'Burger', 'Ajay': 'Roti', 'Shubham': {'Break-Fast': 'Maggie', 'Lunch': 'chicken', 'Dinner': 'Biryani'}, 'Leena': 'Toffee'}

print(d2.keys()) # dict_keys(['Harry', 'Ajay', 'Shubham', 'Leena'])
print(d2.items()) # dict_items([('Harry', 'Burger'), ('Ajay', 'Roti'), ('Shubham', {'Break-Fast': 'Maggie', 'Lunch': 'chicken', 'Dinner': 'Biryani'}), ('Leena', 'Toffee')])
print(d2.values())


