# create a function called do_n that takes a function 
# object and a number, n as arguements, and that calls 
# the given function n times.

def do_n(hello_function, n):
    if n <= 0:
        return
    hello_function()
    do_n(hello_function, n - 1)


def greetings():
    print('Welcome to the village!')

do_n(greetings, 4)