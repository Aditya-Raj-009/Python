# f1 = open("prince.txt")

try:
    f = open("doesn't.txt")

except Exception as e:
    print(e)

else:
    print("This will run only when except is not running..")

finally:
    print("Run this in anyway...")
    # f.close()
    # f1.close()

print("Important stuff")
