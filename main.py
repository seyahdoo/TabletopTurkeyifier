from tkinter import filedialog
import os
import shutil


def get_path():

    path = None

    while True:
        path = filedialog.askdirectory(initialdir='~/Documents/My Games/Tabletop Simulator')
        if os.path.isdir(path + "/Mods"):
            break
        else:
            print(
                "You must show the folder inside Documents named \"Tabletop Simulator\" with \"Mods\" folder inside it.")

    return path


def do_backup(path):
    if not os.path.isdir(path + "BACKUP"):
        print("No Backup Found: Backing up to -> " + path + "BACKUP")
        shutil.copytree(path, path + "BACKUP")


def inplace_change(file_path, old_string, new_string):

    with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
        s = f.read()
        if old_string not in s:
            return

    with open(file_path, 'w', encoding='utf8') as f:
        s = s.replace(old_string, new_string)
        f.write(s)


def replace_mod_files(path):
    # Replace http imgur and pastebin links to https
    json_files = [pos_json for pos_json in os.listdir(path) if pos_json.endswith('.json')]

    for file in json_files:
        inplace_change(path + file, "http://imgur.com", "https://imgur.com")
        inplace_change(path + file, "http://i.imgur.com", "https://i.imgur.com")
        inplace_change(path + file, "http://pastebin.com", "https://pastebin.com")


def rename_downloaded_files(path):

    for filename in os.listdir(path):

        dst = filename
        dst = dst.replace("httpimgurcom", "httpsimgurcom")
        dst = dst.replace("httppastebincom", "httpsiimgurcom")
        dst = dst.replace("httpiimgurcom", "httpsiimgurcom")

        src = path + filename
        dst = path + dst

        if src != dst:
            if not os.path.isfile(dst):
                os.rename(src, dst)


if __name__ == "__main__":

    chosen_path = get_path()

    do_backup(chosen_path + "/Mods/Workshop")
    do_backup(chosen_path + "/Saves")

    replace_mod_files(chosen_path + "/Mods/Workshop/")
    replace_mod_files(chosen_path + "/Saves/")

    rename_downloaded_files(chosen_path + "/Mods/Images/")
    rename_downloaded_files(chosen_path + "/Mods/Models/")
