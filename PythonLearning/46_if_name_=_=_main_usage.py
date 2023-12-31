
def printhar(string):
    return f"ye string prince ko de do.{string}"

def add(n1,n2):
    return n1+n2+5

if __name__=='__main__':        # here name is main in this function. so below code execute only in this file.
    print(printhar("Aditya"))
    a = add(6,4)
    print(a)
print(__name__)
# know if I use these function in another file name say "46 continue":
'''then after import 46_if_name_=_=_main_usage 
when we use function this module in 46 continue file
it will execute line no 8 9 and other also which we not want.
to stop this we enclose this in if condition.
here __name__ is name of the file which we import.
'''