l1 = ["Bhindi","Aloo","chopsticks","chowmein"]

# suppose u want only item which is on every 2nd index.
# then:
i=1
for item in l1:
    if i%2 is  0:
        print(f"Jarvis please buy {item}")
    i+=1

# But above way is little bigger. So we use Enumerate function:
for index , item in enumerate (l1):
    if index%2==0:
        print(f"Jarvis please buy {item}")