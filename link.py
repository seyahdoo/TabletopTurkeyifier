import os


def sym_link_already_downloaded_files(p, folder_list):
    # if both files is real, delete proxy file
    # if only proxy file is real, move file original position
    # create sym link for original file to proxy file
    for folder_path in folder_list:

        for filename in os.listdir(folder_path):

            # if this is not a link, and if this is a proxified file
            file_path = os.path.join(folder_path, filename)
            if (not os.path.islink(file_path)) and (p.is_proxy_or_original(filename) != "irrelevant"):

                original_name = None
                proxy_name = None
                original_path = None
                proxy_path = None

                # if proxy, delete original and rename this to be original
                if p.is_proxy_or_original(filename) == "proxy":
                    proxy_name = filename
                    proxy_path = os.path.join(folder_path, proxy_name)
                    original_name = p.get_original_from_proxy_non_special(filename)
                    original_path = os.path.join(folder_path, original_name)
                    if os.path.isfile(original_path):
                        # print("removing" + folder_path + original_name)
                        os.remove(original_path)
                    # print("renaming" + folder_path + proxy_name + " to " + folder_path + original_name)
                    os.rename(proxy_path, original_path)

                # if original, delete proxy,
                elif p.is_proxy_or_original(filename) == "original":
                    original_name = filename
                    original_path = os.path.join(folder_path, original_name)
                    proxy_name = p.get_proxy_from_original_non_special(filename)
                    proxy_path = os.path.join(folder_path, proxy_name)
                    if os.path.isfile(proxy_path):
                        # print("removing" + folder_path + proxy_name)
                        os.remove(proxy_path)

                # now only original file exists
                # link original to proxy
                # so the game wont re-download it. (for host that will not be using this program)
                # print("linking" + folder_path + original_name + " to " + folder_path + proxy_name)
                os.symlink(original_path, proxy_path)

            # if this is an invalid link, delete it
            elif os.path.islink(file_path):
                if not os.path.exists(os.readlink(file_path)):
                    print("invalid link detected, deleting " + file_path)
                    os.remove(file_path)
    return
