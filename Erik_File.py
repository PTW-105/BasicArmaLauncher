# IMPORTS
import os
import hashlib


# GLOBAL VARIABLES
g_variable = []
g_npm = 0
move = 1
# FUNCTIONS
def param():
    pass


move = 1
g_npm = 0
while move == 1:
        print("Number of Parameters Entered", g_npm)
        i = input("Enter a Parameter: ")
        g_variable.append(i)
        call = input("Add Another Parameter?(Yes,No) ")
        if call == "Yes":
            move = 1
            print("Continuing Parameter Input")
            g_npm += 1
        else:
            move = 0
            print("Exiting Parameter Input...")
            print("Parameters Selected:")
x = 0
for x in g_variable:
    print(x)