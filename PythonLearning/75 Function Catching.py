import time


def some_work(n):
    # some task taking n seconds
    time.sleep(n)
    return n


# if __name__ == '__main__':
#     print("Now running some_work...")
#     print(some_work(3))
#     print("Done....calling again.....")
#     print(some_work(3))
#     print("called again....")

#  ab maanlo mujhe phir se same number ke liye iss function ka jaroorat pad gaya ,
#  to kya phir se utne second ke liye wait karna hog?
#  That's why we use Function catching.

# function caching : Function caching allows us to cache the return values of a function depending on the arguments.
# Tt can save time when I/O bound function is periodically called with same arguments. so we have to import lru from functools:

from functools import lru_cache


@lru_cache(maxsize=6)  # maxsize use for number of value u want to catch. more the number u put more will be the memory occupied.
def some_work2(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Now running some_work...")
    print(some_work2(3))
    print("Done....calling again.....")
    print(some_work2(6))
    print("Done....calling again.....")
    print(some_work2(6))
    print("Done....calling again.....")
    print(
        some_work2(3))  # now this it will not take 3 sec to execute. it will execute as soon as previous line is done.
    print("called again....")
