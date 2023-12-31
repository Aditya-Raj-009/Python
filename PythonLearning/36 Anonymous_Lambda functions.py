# Lambda or Anonymous function:

def add(a,b):
    return a+b

# But if i don't want to make function for add then I should use  lambda:
#  lambda ko humlog function bol v sakte h aur nahi v:

sum = lambda a,b: a+b

print(sum(2,4)) # 6


#  function for sort a list by comparing only first index of every sub list:
def a_first(a):
    return a[1]

a = [[1,14],[2,18],[4,15]]
# a.sort(key=a_first)
# print(a)

#  Now the same by using lambda:
a.sort(key=lambda a:a[1]) # do the same thing.
print(a)