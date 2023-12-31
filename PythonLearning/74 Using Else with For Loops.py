khana = ["roti", "Sabji", "chawal"]

for item in khana:
    print(item)

else:
    print("this for loop ended properly")  # else with for loop works only when for loop ended properly.
    # else will not execute when for loop not able to iterate for all its values...ie. if we apply break statement:

for i in khana:
    print(i)
    break

else:
    print("this for loop ended.")   # this time else will not execute.
