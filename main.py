from tkinter import Tk
from tkinter import filedialog
import os
import shutil
import sys, time, msvcrt
import locale

proxies = {
    "imgur.com": "filmot.org",
    "pastebin.com": "pastebin.seyahdoo.com",
    "cubeupload.com": "cubeupload.seyahdoo.com",
    "https://filmot.org": "http://filmot.org",
    "https://i.filmot.org": "http://i.filmot.org",
    "https://pastebin.seyahdoo.com": "http://pastebin.seyahdoo.com",
    "https://cubeupload.seyahdoo.com": "http://cubeupload.seyahdoo.com"
}

words = [
    {
        'en': "Finding mods root path",
        'tr': "Mod kök dosyası bulunuyor"
    },{
        'en': "Backing up intial data",
        'tr': "Orjinal dosyalar yedekleniyor"
    },{
        'en': "Changing blocked url's inside Json mod files with proxy url's",
        'tr': "Json mod dosyaları içindeki blocklanmış url'ler proxy'leriyle değiştiriliyor."
    },{
        'en': "Fixing previously downloaded Image and Model cache names vith SymLinks",
        'tr': "Önceden indirilmiş Resimler ve Modellerin isimleri linklenerek düzeltiliyor"
    },{
        'en': "DONE!",
        'tr': "BİTTİ!"
    },{
        'en': "Press Enter to continue...",
        'tr': "Çıkmak için Enter'a basınız..."
    }
]


def get_localized_string(locale, string_no):
    if locale == 'tr':
        return words[string_no]['tr']
    else:
        return words[string_no]['en']


def get_de_specialized_string(string):
    return ''.join(e for e in string if e.isalnum())


def get_mods_root_path():
    path = os.path.expanduser("~/Documents/My Games/Tabletop Simulator/")
    while True:
        if os.path.isdir(path + "/Mods"):
            break
        elif path == "":
            print("No folder selected, exiting program.")
            exit(0)
        else:
            print(
                "You must show the folder inside Documents "
                "named \"Tabletop Simulator\" with \"Mods\" folder inside it."
            )

        root = Tk()
        root.withdraw()
        path = filedialog.askdirectory(
            initialdir=path,
            title='Choose root of Tabletop Simulator Mods folder.'
        )
    return path


def do_backup_folder(file_path):
    if not os.path.isdir(file_path + "BACKUP"):
        print("No Backup Found: Backing up to -> " + file_path + "BACKUP")
        shutil.copytree(file_path, file_path + "BACKUP")


def replace_string_inside_file(file_path, old_string, new_string):
    with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
        s = f.read()
        if old_string not in s:
            return
    with open(file_path, 'w', encoding='utf8') as f:
        s = s.replace(old_string, new_string)
        f.write(s)


def proxify_mod_files_in_folder(file_path):
    # Replace http imgur and pastebin links to https
    json_files = [pos_json for pos_json in os.listdir(file_path) if pos_json.endswith('.json')]
    for file_name in json_files:
        for original, proxy in proxies.items():
            replace_string_inside_file(file_path + file_name, original, proxy)
    subfolders = [f.path for f in os.scandir(file_path) if f.is_dir()]
    for subfolder in subfolders:
        proxify_mod_files_in_folder(subfolder + "\\")

def is_proxy_or_original(string):
    for original, proxy in proxies.items():
        if original in string or get_de_specialized_string(original) in string:
            return "original"
        if proxy in string or get_de_specialized_string(proxy) in string:
            return "proxy"
    return "none"


def get_proxy_from_original_nonspecial(string):
    r = string
    for original, proxy in proxies.items():
        r = r.replace(get_de_specialized_string(original), get_de_specialized_string(proxy))
    return r

def get_original_from_proxy_nonspecial(string):
    r = string
    for original, proxy in proxies.items():
        r = r.replace(get_de_specialized_string(proxy), get_de_specialized_string(original))
    return r

def sym_link_already_downloaded_files(file_path):
    # if both files is real, delete proxy file
    # if only proxy file is real, move file original position
    # create sym link for original file to proxy file
    for filename in os.listdir(file_path):
        if (not os.path.islink(file_path + filename)) and (is_proxy_or_original(filename) != "none"):
            # if proxy, delete original
            original_name = None
            proxy_name = None
            if is_proxy_or_original(filename) == "proxy":
                proxy_name = filename
                original_name = get_original_from_proxy_nonspecial(filename)
                if os.path.isfile(file_path + original_name):
                    os.remove(file_path + original_name)
                os.rename(file_path + proxy_name, file_path + original_name)

            elif is_proxy_or_original(filename) == "original":
                original_name = filename
                proxy_name = get_proxy_from_original_nonspecial(filename)
                # if proxy file exists, delete it and link it
                if os.path.isfile(file_path + proxy_name):
                    os.remove(file_path + proxy_name)

            # now only original file exists
            # link original to proxy
            os.symlink(file_path + original_name, file_path + proxy_name)
        elif os.path.islink(file_path + filename):
            if not os.path.exists(os.readlink(file_path + filename)):
                os.remove(file_path + filename)


def wait_enter_or_seconds(caption, timeout = 5):

    start_time = time.time()
    sys.stdout.write('%s'%(caption))
    sys.stdout.flush()
    input = ''
    while True:
        if msvcrt.kbhit():
            byte_arr = msvcrt.getche()
            if ord(byte_arr) == 13: # enter_key
                break
            elif ord(byte_arr) >= 32:  # space_char
                input += "".join(map(chr, byte_arr))
        if len(input) == 0 and (time.time() - start_time) > timeout:
            break

    print('')  # needed to move to next line
    return input


if __name__ == "__main__":

    lang = locale.getdefaultlocale()[0].split('_')[0]

    # intro
    print("##########################################")
    print("##########################################")
    print("####                                  ####")
    print("####    TABLETOP TURKEYIFIER v1.1.0   ####")
    print("####                                  ####")
    print("####           created by seyahdoo    ####")
    print("####                                  ####")
    print("##########################################")
    print("##########################################")
    print()
    print()

    # Getting root mods path
    print(get_localized_string(lang,0))
    root_path = get_mods_root_path()

    # Backing up intial data
    print(get_localized_string(lang,1))
    do_backup_folder(root_path + "/Mods/Workshop")
    do_backup_folder(root_path + "/Saves")

    # Proxying json mod files
    print(get_localized_string(lang,2))
    proxify_mod_files_in_folder(root_path + "/Mods/Workshop/")
    proxify_mod_files_in_folder(root_path + "/Saves/")

    # Fixing previously downloaded Image and Model cache
    print(get_localized_string(lang,3))
    sym_link_already_downloaded_files(root_path + "/Mods/Images/")
    sym_link_already_downloaded_files(root_path + "/Mods/Models/")

    # DONE!
    print(get_localized_string(lang,4))

    # Press Enter to continue...
    wait_enter_or_seconds(get_localized_string(lang,5), 3)

