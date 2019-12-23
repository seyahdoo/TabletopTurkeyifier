from sys import exit
from localization import get_localized_string, print_localized
from path import get_paths, get_documents_root
from backup import do_backup_folder
from proxify import Proxify
from link import sym_link_already_downloaded_files
from request_admin import admin_or_exit
from updater import update_app
from version import version


if __name__ == "__main__":

    # intro
    print("##########################################")
    print("##########################################")
    print("####                                  ####")
    print("####    TABLETOP TURKEYIFIER          ####")
    print("####                                  ####")
    print("####           created by seyahdoo    ####")
    print("####                                  ####")
    print("##########################################")
    print("##########################################")
    print()
    print("version = " + version)

    # Try to update self
    just_updated = update_app()

    # Getting root mods path
    print_localized("find_root")
    mods_list, asset_folder_list = get_paths()

    # Backing up intial data
    print_localized("backup")
    for mod_path in mods_list:
        do_backup_folder(mod_path)

    p = Proxify()

    history_location = "{}\\TurkeyifierHistory.json".format(get_documents_root())

    # Proxying json mod files
    p.load_proxy_history(history_location)

    if just_updated:
        # Revert old proxies
        p.proxify_mod_files_in_folder_list(mods_list, True)
        p.reset_proxy_history(history_location)

    # Do proxy calculations and save
    p.proxify_mod_files_in_folder_list(mods_list, False)
    p.save_proxy_history(history_location)

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
