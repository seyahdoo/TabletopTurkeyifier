import os

from util import *

proxies = {
    "imgur.com": "filmot.org",
    "pastebin.com": "pastebin.seyahdoo.com",
    "cubeupload.com": "cubeupload.seyahdoo.com",
    "https://filmot.org": "http://filmot.org",
    "https://i.filmot.org": "http://i.filmot.org",
    "https://pastebin.seyahdoo.com": "http://pastebin.seyahdoo.com",
    "https://cubeupload.seyahdoo.com": "http://cubeupload.seyahdoo.com",
    "https://u.cubeupload.seyahdoo.com": "http://u.cubeupload.seyahdoo.com"
}


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


def is_proxy_or_original(string):
    # detect if a file is proxified, original or unrelated
    for original, proxy in proxies.items():
        if original in string or get_de_specialized_string(original) in string:
            return "original"
        if proxy in string or get_de_specialized_string(proxy) in string:
            return "proxy"
    return "unrelated"


def proxify_mod_files_in_folder(file_path):

    # Replace blocked links with proxy links inside json files
    json_files = [pos_json for pos_json in os.listdir(file_path) if pos_json.endswith('.json')]
    for file_name in json_files:
        for original, proxy in proxies.items():
            replace_string_inside_file(file_path + file_name, original, proxy)

    # recursively proxify sub folders
    subfolders = [f.path for f in os.scandir(file_path) if f.is_dir()]
    for subfolder in subfolders:
        proxify_mod_files_in_folder(subfolder + "\\")

    return