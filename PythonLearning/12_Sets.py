# Sets :

s = set()  # Empty set.
print(type(s))      # <class 'set'>

# Add elements in set:
s.add(3)
s.add(4)
s.add(2)
s.add(1)
print(s)  # {1, 2, 3, 4}

# set functions:

s1 = s.union({2,4,7})
print(s1) # {1, 2, 3, 4, 7}, jo v unique hoga wo set me add ho kr return ho jaega.
s2 = s.intersection({2,4,7})
print(s2)   # {2, 4}, jo common hota h wo he print hota h.
print(len(s)) # 4
print(max(s))
print(min(s))
s3 = {3,4}
print(s.isdisjoint(s3)) # False
s.remove(4)
print(s) # {1, 2, 3}


# there is an alternative way to make set and that is by using list:

set_from_list = set([1,3,5,2,6])
print(type(set_from_list))  # <class 'set'>
print(set_from_list)    # {1, 2, 3, 5, 6}, element automatically arrange in sorted manner.
            # OR:
list = [3,6,2,1]
print(set(list))    # {1, 2, 3, 6}

