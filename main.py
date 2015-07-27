# IMPORTS
import os
import winreg
import hashlib


# GLOBAL VARIABLES
g_variable = ""


# FUNCTIONS
def main():

    find_steam_dir()

def execute():
    os.system('')


def find_steam_dir():
    l_steam_directory = ""
    l_steam_dir_found = False
    l_possible_steam_dirs = ['C:\\Program Files\\Steam\\steamapps\\common\\']

#    l_steam_reg_path = r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 107410"
    l_steam_reg_path = r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall'
    l_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 107410', 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_ALL_ACCESS))
    val = winreg.QueryValue(l_key, "InstallLocation")
    return(val)

main()