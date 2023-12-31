def strobogrammatic_num(n:int):
    return numdef(n,n)

def numdef(n,length):
    if n==0: return [""]
    if n==1: return ["1","0","8"]
    middles = numdef(n-2,length)
    result = []
    for m in middles:
        if n!=length:
            result.append("0"+m+"0")
        result.append("8" + m + "8")
        result.append("1" + m + "1")
        result.append("9" + m + "6")
        result.append("6" + m + "9")
    return  result

if __name__ == '__main__':
    print(strobogrammatic_num(4))
