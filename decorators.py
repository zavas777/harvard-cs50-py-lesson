def announce(f):

    def wrapper():
        print("About to run the function")
        f()
        print("Ran the function")

    return wrapper

# announce(f) returns a new function based on f

@announce
def hello(): 
    print("Hello, Multiverse!")

hello()




