import os
from sys import exit, platform
from tkinter import Tk
from tkinter import filedialog
import winreg
import vdf

from localization import get_localized_string, print_localized


def get_paths():
    mods_paths = []
    asset_folder_paths = []

    documents_path = get_documents_root()
    install_path = find_steam_app_install_path("286160")
    possible_root_paths = [documents_path, install_path]

    for path in possible_root_paths:
        if os.path.isdir(path + "/Mods/Workshop/"):
            mods_paths.append(path + "/Mods/Workshop/")
        if os.path.isdir(path + "/Saves/"):
            mods_paths.append(path + "/Saves/")

        if os.path.isdir(path + "/Mods/Assetbundles/"):
            asset_folder_paths.append(path + "/Mods/Assetbundles/")
        if os.path.isdir(path + "/Mods/Audio/"):
            asset_folder_paths.append(path + "/Mods/Audio/")
        if os.path.isdir(path + "/Mods/Images/"):
            asset_folder_paths.append(path + "/Mods/Images/")
        if os.path.isdir(path + "/Mods/Images Raw/"):
            asset_folder_paths.append(path + "/Mods/Images Raw/")
        if os.path.isdir(path + "/Mods/Models/"):
            asset_folder_paths.append(path + "/Mods/Models/")
        if os.path.isdir(path + "/Mods/Models Raw/"):
            asset_folder_paths.append(path + "/Mods/Models Raw/")
        if os.path.isdir(path + "/Mods/PDF/"):
            asset_folder_paths.append(path + "/Mods/PDF/")
        if os.path.isdir(path + "/Mods/Text/"):
            asset_folder_paths.append(path + "/Mods/Text/")

    return mods_paths, asset_folder_paths


def get_mods_root_path():
    path = os.path.expanduser("~/Documents/My Games/Tabletop Simulator/")
    while True:
        if os.path.isdir(path + "/Mods") and os.path.isdir(path + "/Mods/Workshop"):
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


def get_documents_root():
    return os.path.expanduser("~/Documents/My Games/Tabletop Simulator/")


def find_steam_app_install_path(app_id):
    steam_path = find_steam_install_path()
    library_folders = [steam_path]

    v = vdf.load(open('{}\\steamapps\\libraryfolders.vdf'.format(steam_path)))
    lf = v["LibraryFolders"]

    i = 1
    while True:
        try:
            folder_path = lf[str(i)]
            library_folders.append(folder_path)
            i += 1
        except:
            break

    for library_folder in library_folders:
        path = library_folder + "/steamapps/appmanifest_{}.acf".format(app_id)
        if os.path.isfile(path):
            manifest = vdf.load(open(path))
            name = manifest["AppState"]["name"]
            return "{}/steamapps/common/{}".format(library_folder, name)

    return ""


def find_steam_install_path():
    try:
        registry_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Wow6432Node\Valve\Steam",
            0,
            winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, "InstallPath")
        winreg.CloseKey(registry_key)
        return value
    except:
        pass

    try:
        registry_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Valve\Steam",
            0,
            winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, "InstallPath")
        winreg.CloseKey(registry_key)
        return value
    except:
        pass

    return ""
