
# Lists and list function:

grocery = ["Harpic", "vim bar", "deodrant", "Bhindi", "Lollipop",54,89,78]
print(grocery)

mylist = [67,77,90] # list with no items
numbers = [4,5,6,3,64,63]
print(numbers)

# accesing items from list:
print(grocery[0]) # Harpic
print(grocery[3]) # Bhindi
print(grocery[7]) # 78

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])

# List functions:

'''
.sort() :  sort your original list in ascending order.
.reverse(): sort your original list in descending order.
len(list): return length of the list.
max(list) : return max element of the list.
min(list) : return min element of the list. 
.append(item or a list) : add items or a list at the end of the list.
.insert(index, item or a list) : add item or a list at specified index of the list.
.remove(item): remove item from list.
.pop(index or no argument): if u pass nothing i.e no argument then it just remove the item from the end of the list.
                            And when u pass the index then it remove the item from that specified index.
'''
numbers.sort() # sort original list.
print(numbers)

numbers.reverse()
print(numbers)

print(len(numbers)) # 6
print(max(numbers)) # 64
print(min(numbers)) # 3

numbers.append(88)
print(numbers) # [64, 63, 6, 5, 4, 3, 88]

# numbers.append(mylist)
# print(numbers) # [64, 63, 6, 5, 4, 3, 88, [67, 77, 90]]

numbers.insert(4,20)
print(numbers) # [64, 63, 6, 5, 20, 4, 3, 88, [67, 77, 90]]

# numbers.insert(4,mylist)
# print(numbers) # [64, 63, 6, 5, [67, 77, 90], 20, 4, 3, 88, [67, 77, 90]]

numbers.remove(88)
print(numbers) # [64, 63, 6, 5, 20, 4, 3]

numbers.pop()
print(numbers) # [64, 63, 6, 5, 20, 4] remove item from end of the list.
numbers.pop(1) # [64, 6, 5, 20, 4] remove item from index 1.
print(numbers)

# slicing of list:

print(numbers[0:5]) #[64, 63, 6, 5, 4, 3]
print(numbers[:5]) #[64, 63, 6, 5, 4, 3]
print(numbers[:]) #[64, 63, 6, 5, 4, 3]
print(numbers[3:]) #[5, 4, 3]
print(numbers[2:5]) #[6, 5, 4]
# extended slicing:
print(numbers[::]) # [64, 63, 6, 5, 4, 3]
print(numbers[::2]) # [64, 6, 4] skip one-one
print(numbers[::-2]) # [3, 5, 63] first reverse the list then skip by one
print(numbers[::-1]) # [3, 4, 5, 6, 63, 64]


# tuples:

# tuples are imutable i.e. you cannot change its value. While lists are mutable i.e. you can change its value.

tp = (1,5,3,8)  # tuple
print(tp) # (1, 5, 3, 8)
# tp[1] = 9
# print(tp) throw error as u cannot change the values of tuple.

tp2 = (3)
print(tp2) # 3 focus that know 3 is not in ().

# So when u creating a tuple contains only one element then it must be creating like this --> tp3 = (3,) :
tp3 = (3,)
print(tp3) # (3,)

# Swapping values:

# general technique:
a = 6
b =4
temp = a
a = b
b = temp
print(a, b) # a=4 b=6

# but there is a special technique in python to swap values:
c=3
d=9
c,d = d,c
print(c,d) # c=9 d=3