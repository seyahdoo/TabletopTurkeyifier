import os
from tkinter import Tk
from tkinter import filedialog

from localization import get_localized_string


def get_mods_root_path():
    path = os.path.expanduser("~/Documents/My Games/Tabletop Simulator/")
    while True:
        if os.path.isdir(path + "/Mods"):
            break
        elif path == "":
            print(get_localized_string("say_no_folder"))
            exit(0)
        else:
            print(get_localized_string("say_show_file"))

        root = Tk()
        root.withdraw()
        # TODO localize
        path = filedialog.askdirectory(
            initialdir=path,
            title=get_localized_string("say_choose_root")
        )
    return path
