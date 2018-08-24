from sys import exit

from localization import get_localized_string, print_localized
from util import wait_enter_or_seconds
from auto_update import update_app
from path import get_mods_root_path
from backup import do_backup_folder
from proxify import proxify_mod_files_in_folder
from link import sym_link_already_downloaded_files


version = "1.2.6"


if __name__ == "__main__":

    # intro
    print("##########################################")
    print("##########################################")
    print("####                                  ####")
    print("####    TABLETOP TURKEYIFIER v{}   ####".format(version))
    print("####                                  ####")
    print("####           created by seyahdoo    ####")
    print("####                                  ####")
    print("##########################################")
    print("##########################################")
    print()
    print()

    # Try to update self
    update_app(version)

    # Getting root mods path
    print_localized("find_root")
    root_path = get_mods_root_path()

    # Backing up intial data
    print_localized("backup")
    do_backup_folder(root_path + "/Mods/Workshop")
    do_backup_folder(root_path + "/Saves")

    # Proxying json mod files
    print_localized("changing_url")
    proxify_mod_files_in_folder(root_path + "/Mods/Workshop/")
    proxify_mod_files_in_folder(root_path + "/Saves/")

    # Fixing previously downloaded Image and Model cache
    print_localized("fixing_links")
    sym_link_already_downloaded_files(root_path + "/Mods/Images/")
    sym_link_already_downloaded_files(root_path + "/Mods/Models/")

    # DONE!
    print_localized("done")

    # Press Enter to continue...
    wait_enter_or_seconds(get_localized_string("press_enter"), 3)

    exit(0)
