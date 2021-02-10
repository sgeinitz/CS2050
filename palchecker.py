import unittest
from deque_complete import Deque

def palCheck(orig_input_string):
    """ A function to check whether a string is palindrome """
    d = Deque()

    input_string = orig_input_string
    
    # copy the input_string to our deque object one character at a time
    for char in input_string:
        d.addRear(char)

    while d.size() > 1:
        firstChar = d.removeRear()
        lastChar = d.removeFront()
        if firstChar != lastChar:
            print("No, '" + orig_input_string + "', is not a palidrome")
            return False

    print("Yes, '" + orig_input_string + "', is a palidrome!")
    return True
