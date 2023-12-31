f = open("prince.txt")
# print(f.readline()) # read first line.
# print(f.readline()) # read second line.
# print(f.readline()) # read third line.

# to get know where is your file pointer, we use .tell() function. This function tell us location of pointer:
# print(f.tell()) # 0
# print(f.readline()) # read first line.
# print(f.tell()) # 28
# print(f.readline()) # read second line.
# print(f.tell()) # 88
# print(f.readline()) # read third line.
# print(f.tell()) # 109

# to reset file pointer we use .seek() function. This function bring your pointer to specify location:
print(f.readline())
f.seek(0)
print(f.readline()) # again print previous line(as we use seek())
f.seek(0)
print(f.readline()) # again print previous line(as we use seek())
f.close()