import os


def sym_link_already_downloaded_files(p, file_path):
    # if both files is real, delete proxy file
    # if only proxy file is real, move file original position
    # create sym link for original file to proxy file

    for filename in os.listdir(file_path):

        # if this is not a link, and if this is a proxified file
        if (not os.path.islink(file_path + filename)) and (p.is_proxy_or_original(filename) != "irrelevant"):

            original_name = None
            proxy_name = None

            # if proxy, delete original and rename this to be original
            if p.is_proxy_or_original(filename) == "proxy":
                proxy_name = filename
                original_name = p.get_original_from_proxy_non_special(filename)
                if os.path.isfile(file_path + original_name):
                    os.remove(file_path + original_name)
                os.rename(file_path + proxy_name, file_path + original_name)

            # if original, delete proxy,
            elif p.is_proxy_or_original(filename) == "original":
                original_name = filename
                proxy_name = p.get_proxy_from_original_non_special(filename)
                if os.path.isfile(file_path + proxy_name):
                    os.remove(file_path + proxy_name)

            # now only original file exists
            # link original to proxy
            # so the game wont re-download it. (for host that will not be using this program)
            os.symlink(file_path + original_name, file_path + proxy_name)

        # if this is an invalid link, delete it
        elif os.path.islink(file_path + filename):
            if not os.path.exists(os.readlink(file_path + filename)):
                os.remove(file_path + filename)
    return
