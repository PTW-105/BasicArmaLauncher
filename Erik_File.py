# IMPORTS
import os
import hashlib


# GLOBAL VARIABLES
g_variable = []
g_npm = 0
move = True

# FUNCTIONS
def param():
    pass


while move is True:
        print("Number of Parameters Entered", g_npm)
        i = input("Enter a Parameter: ")
        g_variable.append(i)
        call = input("Add Another Parameter?(Y,N) ")
        call = str.lower(call)
        if call == "y":
            print("Continuing Parameter Input")
            g_npm += 1
        elif call == "n":
            move = False
            print("Exiting Parameter Input...")
            print("Parameters Selected:")
        else:
            fault = False
            while fault is False:
                call2 = input("Invalid Input, Please Try Again: ")
                call2 = str.lower(call2)
                if call2 == "y":
                    print("Continuing Parameter Input")
                    move = True
                    g_npm += 1
                    fault = True
                elif call2 == "n":
                    move = False
                    fault = True
                    print("Exiting Parameter Input...")
                    print("Parameters Selected:")
                else:
                    fault = False
