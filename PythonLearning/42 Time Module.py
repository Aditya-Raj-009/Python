import time

initial = time.time() # time taken by programme in this line.

k = 0
while k<20:
    print("This is Prince!")
    k+=1
print("Time taken by while loop is ",time.time()-initial,"second")

initial2 = time.time() # time taken by programme in this line.
for i in range(20):
    print("This is Prince!")
print("Time taken by for loop is ",time.time()-initial2,"second")

#  to get local time:
localeTime = time.asctime(time.localtime(time.time()))
print(localeTime)

# sleep() function in time:
i=0
while(i!=10):
    print("Hello!")
    time.sleep(2)   # wait for 2 sec then execute.
    i+=1