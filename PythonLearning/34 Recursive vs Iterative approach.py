# def print2(str1):
#     return "This is "+str1
#
# print(print2("Prince"))

# if we want to make a empty method, then we use pass keyword:
def factorial(n):
    '''

    :param n: Integer
    :return: n*n-1 * n-2 * n-3....
    '''

    pass


# Recursion:
def nthFibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return nthFibo(n - 1) + nthFibo(n - 2)


def factorial(n):
    if (n == 1 or n == 0):
        return 1
    return n * factorial(n - 1)


print(factorial(3))
print(nthFibo(7))
