from random import randint
from time import sleep
from tqdm import tqdm, trange


# By using module:

def progressBar(num):
    # rnt = randint(2, 5)
    # for i in tqdm(range(noOfBook)):
    # we can use trange:
    for i in trange(num):
        sleep(0.3)
    print()


# progressBar(100)

# Now we make progress bar by ourself:



def newProgressBar(progress, total):
    percent = 100 * (progress / float(total))  # calculating percent
    bar = "█" * int(percent) + '-' * (100 - int(percent))  # "█" code to get this char is : Alt + 219
    print(f"\r||{bar}|{percent:.2f}%", end="\r")        # \r will just work as you have shifted your cursor to the beginning of the string or line.


for i in range(1000):
    newProgressBar(i + 1, 1000)
    sleep(0.002)
