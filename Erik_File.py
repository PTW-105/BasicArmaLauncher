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
        else:
            move = False
            print("Exiting Parameter Input...")
            print("Parameters Selected:")
x = 0
for x in g_variable:
    print(x)