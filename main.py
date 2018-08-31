from sys import exit

from localization import get_localized_string, print_localized
from util import wait_enter_or_seconds
from auto_update import update_app
from path import get_mods_root_path
from backup import do_backup_folder
from proxify import Proxify
from link import sym_link_already_downloaded_files
from request_admin import admin_or_exit

version = "1.4.0"


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
    is_updated = update_app(version)

    # Getting root mods path
    print_localized("find_root")
    root_path = get_mods_root_path()

    mods_list = [
        root_path + "/Mods/Workshop/",
        root_path + "/Saves/"
    ]

    asset_folder_list = [
        root_path + "/Mods/Images/",
        root_path + "/Mods/Models/",
        root_path + "/Mods/Assetbundles/"
    ]

    # Backing up intial data
    print_localized("backup")
    do_backup_folder(root_path + "/Mods/Workshop")
    do_backup_folder(root_path + "/Saves")

    p = Proxify()

    # Proxying json mod files
    p.load_proxy_history(root_path + "/TurkeyifierHistory.json")

    # if updated, revert old proxies
    if is_updated:
        p.proxify_mod_files_in_folder_list(mods_list, True)
        p.reset_proxy_history(root_path + "/TurkeyifierHistory.json")

    p.proxify_mod_files_in_folder_list(mods_list, False)
    p.save_proxy_history(root_path + "/TurkeyifierHistory.json")

    # Fixing previously downloaded Image and Model cache
    print_localized("fixing_links")
    print_localized("require_admin_for_links")
    admin_or_exit(__file__)
    sym_link_already_downloaded_files(p, asset_folder_list)

    # DONE!
    print_localized("process_finished")
    print_localized("done")

    # Press Enter to continue...
    input(get_localized_string("press_enter"))

    exit(0)
