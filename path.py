import os
from tkinter import Tk
from tkinter import filedialog

from localization import get_localized_string, print_localized


def get_mods_root_path():
    path = os.path.expanduser("~/Documents/My Games/Tabletop Simulator/")
    while True:
        if os.path.isdir(path + "/Mods") \
                and os.path.isdir(path + "/Mods/Workshop") \
                and os.path.isdir(path + "/Saves"):
            break
        elif path == "":
            print_localized("no_folder")
            exit(0)
        else:
            print_localized("show_file")

        root = Tk()
        root.withdraw()
        path = filedialog.askdirectory(
            initialdir=path,
            title=get_localized_string("choose_root")
        )
    return path
