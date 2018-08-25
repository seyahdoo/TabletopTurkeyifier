import os
import re

from util import *

proxies = {
    "https": "http",
    "http://imgur.com": "http://filmot.org",
    "http://i.imgur.com": "http://i.filmot.org",
    "http://pastebin.com": "http://pastebin.seyahdoo.com",
    "http://cubeupload.com": "http://cubeupload.seyahdoo.com",
    "http://u.cubeupload.com": "http://u.cubeupload.seyahdoo.com"
}

proxy_history = {}

non_special_proxy_history = {}

url_expression = re.compile('(\"https?://\S*?((imgur\.com)|(pastebin\.com)|(cubeupload\.com))[^\s"]*\")')


def calculate_proxy(original):
    if "/" not in original:
        if original in non_special_proxy_history:
            return non_special_proxy_history[original]
        return
    else:
        if original in proxy_history:
            return proxy_history[original]
        pass

    proxy = original
    for o, p in proxies.items():
        if proxy.startswith(o):
            proxy = proxy.replace(o, p, 1)

    proxy_history[original] = proxy
    non_special_proxy_history[get_non_specialized_string(original)] = get_non_specialized_string(proxy)

    return proxy


def get_proxy_from_original_non_special(string):
    if string in non_special_proxy_history:
        return non_special_proxy_history[string]
    return


def get_original_from_proxy_non_special(string):
    for original, proxy in non_special_proxy_history:
        if proxy is string:
            return original
    return


def is_proxy_or_original(string):
    # detect if a file is proxified, original or unrelated
    if "/" in string:
        if string in proxy_history.keys():
            return "original"
        elif string in proxy_history.values():
            return "proxy"
        return "irrelevant"
    else:
        if string in non_special_proxy_history.keys():
            return "original"
        elif string in non_special_proxy_history.values():
            return "proxy"
        return "irrelevant"


def proxify_mod_files_in_folder(folder_path):

    # Replace blocked links with proxy links inside json files
    # (without changing modify time so it wont change the order of mods inside game)
    json_files = [pos_json for pos_json in os.listdir(folder_path) if pos_json.endswith('.json')]
    for file_name in json_files:
        file_path = folder_path + file_name
        original_modify_time = os.path.getmtime(file_path)  # capture modify time
        proxify_file(file_path)
        os.utime(file_path, (original_modify_time, original_modify_time))  # restore modify time

    # recursively proxify sub folders
    sub_folders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    for sub_folder in sub_folders:
        proxify_mod_files_in_folder(sub_folder + "\\")

    return


def proxify_file(file_path):
    with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
        s = f.read()
        proxiable_list = url_expression.findall(s)
        if len(proxiable_list) > 0:
            for r in proxiable_list:
                sliced = r[0][1:-1]
                calculate_proxy(sliced)
        else:
            return
    with open(file_path, 'w', encoding='utf8') as f:
        for original, proxy in proxy_history.items():
            s = s.replace(original, proxy)
        f.write(s)
    return
