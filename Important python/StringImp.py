txt = "Welecome"

#center():
print(txt.center(50)) # center method use to center a String.
print(txt.center(50,"*")) # center string with * left and right.

#join(): this method takes all items in an iterable and joins them into one string.
arr = ["Aditya","Raj"]
x = "#".join(arr) # "#" 
print(x)

# split():
name = "Aditya Singh Rajput"
list = name.split(" ")
print(list)

# swapcase(): Make uppercase to lowercase and lowercase to uppercase:
name = "Aditya Raj"
x = name.swapcase()
print(x)

# zfill(): add zeros at the beginning of the string until it reaches the specified length:
num = "50"
k = num.zfill(5)
print(k)