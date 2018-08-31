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

    print_localized("require_admin_for_links")
    admin_or_exit(__file__)

    # Getting root mods path
    print_localized("find_root")
    root_path = get_mods_root_path()

    # Backing up intial data
    print_localized("backup")
    do_backup_folder(root_path + "/Mods/Workshop")
    do_backup_folder(root_path + "/Saves")

    p = Proxify()

    # Proxying json mod files
    p.load_proxy_history(root_path + "/TurkeyifierHistory.json")

    # if updated, revert old proxies
    if is_updated:
        print_localized("reverting_old_version_proxies")
        p.proxify_mod_files_in_folder(root_path + "/Mods/Workshop/", True, True)
        p.proxify_mod_files_in_folder(root_path + "/Saves/", True, True)
        p.reset_proxy_history(root_path + "/TurkeyifierHistory.json")

    print_localized("changing_url")
    p.proxify_mod_files_in_folder(root_path + "/Mods/Workshop/", True, False)
    p.proxify_mod_files_in_folder(root_path + "/Saves/", True, False)

    p.save_proxy_history(root_path + "/TurkeyifierHistory.json")

    # Fixing previously downloaded Image and Model cache
    print_localized("fixing_links")
    sym_link_already_downloaded_files(p, root_path + "/Mods/Images/")
    sym_link_already_downloaded_files(p, root_path + "/Mods/Models/")
    sym_link_already_downloaded_files(p, root_path + "/Mods/Assetbundles/")

    # DONE!
    print_localized("process_finished")
    print_localized("done")

    # Press Enter to continue...
    input(get_localized_string("press_enter"))

    exit(0)
