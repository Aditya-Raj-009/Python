''''
Iterable: Iterable is a object in python for which either __iter__() or __getitem__() method is defined.
when we run this over any object it provide a iterator.

Iterator: Iterator is a object in python for which __next__() method is defined.

Iteration: Traversing a list , tuple, dictionary etc is called Iteration.

Generators : It is a way of creating iterator. simply speaking , a generator is a function that returns
an object (iterator) which we can iterate over (one value at a time). Generator use for save ram.
'''

for i in range(5):  # Range is a type of generator. i.e once we iterate that number,will not able iterate again.
    print(i)


# creating a generator:

def gen(n):
    for i in range(n):
        yield i  # yield is different from return. return means function will return back. but yield will generate a generator.


g = gen(40)
print(type(g))
print(g)  # since we have use yield , output : <generator object gen at 0x000001DE0EF09A10>
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# output: 0 1 2 3 4 (new line)
for i in g:
    print(i)  # print from 5 to 39.this shows, once we iterate that object will not able to iterate again.

# Iterable:

h = "Harry"
itr = iter(h)   # iter() is a generator which return a iterator.
print(type(itr))
print(itr.__next__())   # H
print(itr.__next__())   # a
print(itr.__next__())   # r
print(itr.__next__())   # r
for i in itr:
    print(i)    # will continue and print "y". this shows, once we iterate that object will not able to iterate again.


k = 45455
n = iter(k)
print(n.__next__())  # since int are not iterable , it will throw error.

