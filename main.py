# IMPORTS
import os
import winreg
from subprocess import Popen


# GLOBAL VARIABLES
g_variable = ""


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

main()