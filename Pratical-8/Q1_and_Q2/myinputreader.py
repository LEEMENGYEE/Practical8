def read_integer(promt = "Enter a Integer: ", error = "Error: Wrong Input\n ", minumum = -(10**10), maximum = 10**10):
    """

    Purpose :Read an Integer from user input.
    promt = message , default to the "Enter a Integer "
    error
    minimum = lower bound of user input,default to  -(10**10), maximum = 10**10)
    maximum 

    returm
    
    """

    while True:
        number = input(promt)
        try:
            number = int(number)
            if number >= minumum and number <= maximum:
                return number
            else:
                print(error)
        except ValueError:
            print("Error: Only Integer are Allowed!\n")

def read_floats(promt = "Enter a numbner: ", error = "Error: Wrong Input\n ", minumum = float("-inf"), maximum =float("-inf")):
    """
    Purpose :Read an Integer from user input.

    """

    while True:
        try:
            number = float(input(promt))
            if number >= minumum and number <= maximum:
                return number
            else:
                print(error)
        except:
            print("Error: Only Floating Number is Allowed!")

def read_integers(promt = "Enter a integer: ", error = "Error: Wrong Input\n ", minumum = -(10**10), maximum = 10**10 , stop ="q",loop =10**10):
    integers = []
    count = 0
    stop =str(stop)

    while True:
        integer = input(promt)
        if integer.lower() == stop.lower():
            return integers
        try:
            integer = int(integer)
            if integer >= minumum and integer <=maximum:
                integers.append(integer)
                count += 1
                if count == loop:
                    return integers
            else:
                print(error)
        except ValueError:
            print("Error: ")


def read_floats(promt = "Enter a numbner: ", error = "Error: Wrong Input\n ", minumum = float("-inf"), maximum =float("-inf"), stop = "q" , loop = 10**10):
    """
    Purpose :Read an Integer from user input.

    """

    floats=[]
    count = 0

    while True:
        number = input(promt)
        if number.lower() == stop.lower():
            return floats
        try:
            number = float(number)
            if number >= minumum and number <= maximum:
                floats.append(number)
                count += 1
                if count == loop:
                 return floats
            else:
                print(error)
        except:
            print("Error: Only Floating Number is Allowed!")

def read_string(promt = "Enter a String: "):
    return input(promt).strip()

