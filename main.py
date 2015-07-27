# IMPORTS
import os
import winreg
from subprocess import Popen


# GLOBAL VARIABLES
g_variable = ""
g_param= []
g_npm = 0
move = True

# FUNCTIONS
def main():
    Popen("cmd.exe", shell=True)
    print("Arma 3 install path identified as: " + "'" + dir_find_steam_dir() + "'")


def execute(l_parameters):
    l_steam_dir = "C:\\Games\\steamapps\\common\\Arma 3"
    l_exec_string = Popen(l_steam_dir + "\\arma3.exe" + l_parameters)


def dir_find_steam_dir():
    l_possible_steam_dirs = ['C:\\Program Files\\Steam\\steamapps\\common\\Arma 3',
                             'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Arma 3',
                             'E:\\Program Files\\Steam\\steamapps\\common\\Arma 3',
                             'E:\\Program Files (x86)\\Steam\\steamapps\\common\\Arma 3',
                             'C:\\Games\\steamapps\\common\\Arma 3']

    for path in l_possible_steam_dirs:
        if os.path.isdir(path) is True:
            return path
        elif os.path.isdir(path) is False:
            pass
        else:
            print("ERROR: Path check failed for " + path)
            pass


def reg_find_steam_dir():
    l_steam_directory = ""
    l_steam_dir_found = False
    l_possible_steam_dirs = ['C:\\Program Files\\Steam\\steamapps\\common\\']

#    l_steam_reg_path = r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 107410"
    l_steam_reg_path = r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall'
    l_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 107410', 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_ALL_ACCESS))
    val = winreg.QueryValue(l_key, "InstallLocation")
    return(val)

def param():
    while move is True:
            print("Number of Parameters Entered", g_npm)
            i = input("Enter a Parameter: ")
            g_param.append(i)
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
pass
main()
