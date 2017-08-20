""" Initialisation proof of concept """
import time

def margo_initialisation():
    print ("Margo is initialising...")
    """Insert initialisation code"""
    initstatus = "True"
    return initstatus

def choose_mode():
    selectedmode = True
    while selectedmode:
        print ("Choose operating mode:")
        print ("1 - Input text for processing")
        print ("2 - Input text for speech generation")
        print ()
        selectedmode = raw_input("Enter 1 or 2: ")
        if selectedmode == "1":
            return selectedmode
        elif selectedmode == "2":
            return selectedmode
        else:
            print ("Not Valid - please try again.")

    return