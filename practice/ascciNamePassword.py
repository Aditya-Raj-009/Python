from random import randint

txt = "Aditya"


for i in range(randint(1,len(txt))):
    enc = randint(i,len(txt)-1)
    if txt[enc].isalnum():
        encipted_chr = str(ord(txt[enc]))
        print(f"{txt.replace(txt[enc],encipted_chr)}")

print(f"Your unique password is : {txt}")