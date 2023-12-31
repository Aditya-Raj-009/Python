# importing random module:

import random

# random.randint():
random_number = random.randint(0,5)
print(random_number)

# random.random():
# rand = random.random() # generate random number from 0 to 1 in float.
rand = random.random()*100 # generate random number from 0 to 100 in decimal.
print(rand)

# random.choice() :
list = ["Star plus","Zee tv","Star sport","Nick","Sony max"]
choice = random.choice(list) # choose random values from list.
print(choice)

# random.shuffle():
random.shuffle(list)    # this function shuffle the original list.
print(list)