# f = open("prince.txt","w") # open file for writing.
# f.write("I love coding very much....")
# f.close()

# opening file to append text:
# f = open("prince.txt","a")
# # f.write("\nI have knowledge of java , python, c and web development.")
#
# # to get return of number of character it is written:
# a = f.write("\nI know everything..")
# print(a) # 20.
# f.close()

# Opening file for read and write both:
f = open("prince.txt","r+")
print(f.read()) # reading file.
f.write("\nI enjoy coding a lot..")
f.close()
