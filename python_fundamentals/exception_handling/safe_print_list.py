#!/usr/bin/env python3

"""
Prints up to x elements from my_list on one line.
Returns the actual number of elements printed.
"""

def safe_print_list(my_list=[], x=0):


    try:
        print(x)
    except:
        print("An errors occured")
    finally:
        print("Variables x is not Defined")
    return(x)
