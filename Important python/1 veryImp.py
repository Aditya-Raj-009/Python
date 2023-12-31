# like float,int,string,byte,and other data types there is also one of the best data type in python which is called
#  'eval' this data type take any type of argument. By this we can input any type of data type:
# a = eval(input())
# b = eval(input())
# print(a+b)

# Output:
'''
1 : a = 2, b = 3;(both integer) output: 5
2: a = 4.5,b=3.5;(both float) output: 8.0
3: a = 6.5, b = 3;(a is float and b is integer) output: 9.5
4: a = 0b1010, b = 0b1100; (both are byte a is binary of 10 and b is binary of 12) output : 22
5: a = 0b1010, b = 2; (a is byte and b is integer) output : 12
'''

# Now about range() method in for loop:
'''
rang(5):
from 0 to 4;

range(1,6):
from 1 to 5;

range(1,6,2):
from 1 to 5 by increment of 2.
1,3,5

range(10,0,-2):
from 10 to 1 by decrement of 2.
10,8,6,4,2
'''

#  zip() : this method is use to iterate over 2 list simultaneously:
l = [3,2,4,5]
l2 =[6,2,8,1]
for a,b in zip(l,l2):   # 'a' is for 'l' and 'b' is for 'l2'.
    print(a,b)
# import pywhatkit as wht
# # wht.sendwhatmsg(number to send,msg to send,hour,mint):

# wht.sendwhatmsg("+918252800394","Pushy Cat !",21,58)

# import pyautogui as auto
# import time
#
# time.sleep(5)
#
# for i in range(0):
#     auto.write("Aditya Hacked your phn....!")
#     auto.press("Enter")
