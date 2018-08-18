from tkinter import filedialog
import os
import shutil


def inplace_change(file_path, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
        s = f.read()
        if old_string not in s:
            # print('"{old_string}" not found in {file_path}.'.format(**locals()))
            return

    # Safely write the changed content, if found in the file
    with open(file_path, 'w', encoding='utf8') as f:
        # print('Changing "{old_string}" to "{new_string}" in {file_path}'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)


def do_backup():
    if not os.path.isdir(path + "/Mods/WorkshopBACKUP"):
        print("No Backup Found: Backing up to -> " + path + "/Mods/WorkshopBACKUP")
        shutil.copytree(path + "/Mods/Workshop", path + "/Mods/WorkshopBACKUP")

    if not os.path.isdir(path + "/SavesBACKUP"):
        print("No Backup Found: Backing up to -> " + path + "/SavesBACKUP")
        shutil.copytree(path + "/Saves", path + "/SavesBACKUP")


if __name__ == "__main__":
    # Get Path
    path = None

    while True:
        path = filedialog.askdirectory(initialdir='~/Documents/My Games/Tabletop Simulator')
        if os.path.isdir(path + "/Mods"):
            break
        else:
            print(
                "You must show the folder inside Documents named \"Tabletop Simulator\" with \"Mods\" folder inside it.")

    do_backup()

    # Replace http imgur and pastebin links to https
    json_files = [pos_json for pos_json in os.listdir(path + "/Mods/Workshop") if pos_json.endswith('.json')]

    for file in json_files:
        inplace_change(path + "/Mods/Workshop/" + file, "http://imgur.com", "https://imgur.com")
        inplace_change(path + "/Mods/Workshop/" + file, "http://i.imgur.com", "https://i.imgur.com")
        inplace_change(path + "/Mods/Workshop/" + file, "http://pastebin.com", "https://pastebin.com")

    json_files = [pos_json for pos_json in os.listdir(path + "/Saves") if pos_json.endswith('.json')]

    for file in json_files:
        inplace_change(path + "/Saves/" + file, "http://imgur.com", "https://imgur.com")
        inplace_change(path + "/Saves/" + file, "http://i.imgur.com", "https://i.imgur.com")
        inplace_change(path + "/Saves/" + file, "http://pastebin.com", "https://pastebin.com")

    # TODO also rename already downloaded files

    path_images = path + "/Mods/Images/"

    for filename in os.listdir(path_images):

        dst = filename
        dst = dst.replace("httpimgurcom", "httpsimgurcom")
        dst = dst.replace("httppastebincom", "httpsiimgurcom")
        dst = dst.replace("httpiimgurcom", "httpsiimgurcom")

        src = path_images + filename
        dst = path_images + dst

        if src != dst:
            print(src)
            print(dst)
            os.rename(src, dst)

    path_models = path + "/Mods/Models/"

    for filename in os.listdir(path_models):

        dst = filename
        dst = dst.replace("httpimgurcom", "httpsimgurcom")
        dst = dst.replace("httppastebincom", "httpsiimgurcom")
        dst = dst.replace("httpiimgurcom", "httpsiimgurcom")

        src = path_models + filename
        dst = path_models + dst

        if src != dst:
            print(src)
            print(dst)
            os.rename(src, dst)