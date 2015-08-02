# IMPORTS
import os
import hashlib


# FUNCTIONS
def process_modfolder(l_modfolder):
    """Enumerates and hashes all files in a given Arma 3 modfolder.

    Typical use:
        parse_mods.process_modfolder(modfolder)

    This function accepts a modfolder path and (root relative only) and
    does not return any data.  Instead data is output in a .CSV file
    named 'mod_output_file.csv' in the script current directory.  This
    file contains the following items in order:
    [filename, root-relative path, SHA-1 hash, SHA-256 hash]

    Modify 'output()' function to suite output needs (CSV, XML, SQL, etc.).
    """
    l_mod_files = list_files(l_modfolder)
    for f in l_mod_files:
        l_hashed_return = hash_files(f)
        output(l_hashed_return[0], l_hashed_return[1], l_hashed_return[2], l_hashed_return[3])
    print("Modfolder files successfully enumerated and hashed!  See 'mod_output_file.csv' for output.")
    exit()


def list_files(l_modfolder):
    l_output_list = []

    for root, dirs, files in os.walk(l_modfolder, topdown=True):
        for file in files:
            l_output_list.append([file, root])
    return l_output_list


def hash_files(l_mod_file):
    l_file = l_mod_file[0]
    l_root = l_mod_file[1]
    l_working_file = l_root + "\\" + l_file

    l_mod_file.append(hashlib.sha1(open(l_working_file, 'rb').read()).hexdigest())
    l_mod_file.append(hashlib.sha256(open(l_working_file, 'rb').read()).hexdigest())
    return l_mod_file


def output(l_file, l_dir, l_sha1, l_sha256):
    l_output_string = l_file + ", " + l_dir + ", " + l_sha1 + ", " + l_sha256 + "\n"
    with open('mod_output_file.csv', 'a+') as f:
        f.write(l_output_string)
