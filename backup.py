import os
import shutil

from localization import get_localized_string


def do_backup_folder(file_path):
    backup_path = os.path.join(file_path, "BACKUP")
    if not os.path.isdir(backup_path):
        print(get_localized_string("no_backup_found") + backup_path)
        shutil.copytree(file_path, backup_path)
    return
