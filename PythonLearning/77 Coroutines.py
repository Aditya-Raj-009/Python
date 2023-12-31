# coroutines: coroutine use when we have some function in which there is something which takes time to initialise.
# example below searcher() initially takes 5 sec to search but after that it doesn't take time to search.

def searcher():
    import time
    # some 5 seconds time consuming task:
    book = "this is a very good book.This book wrote by prince.you will surely love it."
    time.sleep(5)  # if we want that when we call first time, it will run till here, and from second time run from next line,
    # we use coroutines because this take some much time:

    while True:
        text = (yield)  # in bracket yield indicating that we are using this searcher as coroutine. After this, this function is coroutine not a function.
        if text in book:
            print("Your text is in the book")

        else:
            print("Text is not in the book")
        print("running....")


search = searcher()
print("Search started...")
next(search)  # to iterate.
print("next method run..")
search.send("prince")  # Your text is in the book. (take 5 sec to execute)
input('Press any key!')     # put input so that you can see that it will not take to execute as soon as you hit input.
search.send("wrote by")     # now it will not take time to execute. i.e.this time function will run from text = (yield).
input('Press any key!')
search.send("fine")     # now it will not take time to execute. i.e.this time function will run from text = (yield).
search.close()  # to release your resources.
# since we have close , if we try to search again it will throw an error:
search.send("very good")
