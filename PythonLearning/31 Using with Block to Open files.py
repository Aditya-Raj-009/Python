# open file by using "with" block:
import os

with open("prince.txt") as f:   # we use with block to open file so that we doesn't need to close the file, It automatically close the file.
    content = f.read()
    print(content)

    if os.path.exists("prince.txt"):  # check whether file exist or not.
        print("file exists")
    else:
        print("File doesn't exist")