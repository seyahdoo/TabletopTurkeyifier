import os
import shutil

from localization import get_localized_string


def do_backup_folder(file_path):
    if not os.path.isdir(file_path + "BACKUP"):
        print(get_localized_string("say_no_backup_found") + file_path + "BACKUP")
        shutil.copytree(file_path, file_path + "BACKUP")
    return
