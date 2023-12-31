# guess number:
import random

num = random.randint(1, 50)
c = 0
i = 0
print("Guess the number between 1 to", num + random.randint(1, 10))
g = random.randint(5, 10)
print("You get only", g, "chance for guess")
while True:
    ch = int(input("Choose number :"))
    i += 1
    c += 1
    if i == g:
        print("Game Over! Original number was", num, ",you tried", c, "times")
        break
    else:
        if num == ch:
            print("Congrats! you have choose the number in", c, "times")
            break
        elif ch > num:
            print("High, you left with", g - i, "chance")
        else:
            print("Low,you left with", g - i, "chance")
