# IMPORTS
import os


# FUNCTIONS
def list_modfolders(l_game_dir):
    """Outputs Arma 3 modfolders present in a given directory.

    Typical use:
        a3_mod_folders = modDetection.list_modfolders(game_directory)
        print(a3_mod_folders) == ['@mod1', '@mod2', '@mod3', ... '@modx']

    This function takes a file system path (root relative or directory relative)
    and returns a list of Arma 3 modfolders within that directory.
    """
    l_modfolders = []
    directories = os.listdir(l_game_dir)
    for d in directories:
        if d.startswith('@'):
            l_modfolders.append(d)
        else:
            pass

    return l_modfolders