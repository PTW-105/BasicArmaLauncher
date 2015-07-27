# IMPORTS
import os
import winreg
from subprocess import Popen


# GLOBAL VARIABLES
g_variable = ""


# FUNCTIONS
def main():
    Popen("cls", shell=True)
    l_steam_dir = dir_find_steam_dir()
    print("Arma 3 install path identified as: " + "'" + l_steam_dir + "'")
    l_parameters = parameters()
    execute(l_steam_dir, l_parameters)


def execute(l_steam_dir, l_parameters):
#    l_exec_string = Popen(l_steam_dir + "\\arma3.exe" + l_parameters)
#    print(l_steam_dir + "\\arma3.exe" + " -mod=" + l_parameters)
    Popen(l_steam_dir + "\\arma3.exe" + " -mod=" + l_parameters)


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
    return val


def parameters():
    l_param = []
    l_npm = 0
    l_move = True
    while l_move is True:
        print("Number of Parameters Entered", l_npm)
        i = input("Enter a Parameter: ")
        l_param.append(i)
        call = input("Add Another Parameter?(Y,N) ")
        call = str.lower(call)
        if call == "y":
            print("Continuing Parameter Input")
            l_npm += 1
        elif call == "n":
            l_move = False
            print("Exiting Parameter Input...")
            print("Parameters Selected:")
        else:
            fault = False
            while fault is False:
                call2 = input("Invalid Input, Please Try Again: ")
                call2 = str.lower(call2)
                if call2 == "y":
                    print("Continuing Parameter Input")
                    l_move = True
                    l_npm += 1
                    break
                elif call2 == "n":
                    l_move = False
                    print("Exiting Parameter Input...")
                    print("Parameters Selected:")
                    break
                else:
                    fault = False

    l_param = "".join(l_param)
    return l_param


main()
