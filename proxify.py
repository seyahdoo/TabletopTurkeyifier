import os
import re
import json

from util import *
from localization import get_localized_string, print_localized

class Proxify:

    def __init__(self):
        self.proxies = {
            "https:": "http:",
            "http://imgur.com": "http://imgur.seyahdoo.com",
            "http://i.imgur.com": "http://i.imgur.seyahdoo.com",
            "http://pastebin.com": "http://pastebin.seyahdoo.com",
            "http://cubeupload.com": "http://cubeupload.seyahdoo.com",
            "http://u.cubeupload.com": "http://u.cubeupload.seyahdoo.com"
        }

        self.known_extensions = [
            "png",
            "jpg",
            "jpeg",
            "obj",
            "unity3d"
        ]

        self.proxy_history = {}
        self.non_special_proxy_history = {}
        self.url_expression = re.compile(
            '(\"https?://((imgur\.com)|(i\.imgur\.com)|(pastebin\.com)|(cubeupload\.com)|(u\.cubeupload\.com))[^\s"]*\")')


    def calculate_proxy(self, original):
        if "/" not in original:
            if original in self.non_special_proxy_history:
                return self.non_special_proxy_history[original]
            return
        else:
            if original in self.proxy_history:
                return self.proxy_history[original]
            pass

        proxy = original
        for o, p in self.proxies.items():
            if proxy.startswith(o):
                proxy = proxy.replace(o, p, 1)

        if proxy is original:
            print("this is not proxified, some kind of error must be happening.")
            print(proxy)
            return

        # print(get_localized_string("adding_new_proxy") + " -> " + original + ":" + proxy)
        self.proxy_history[original] = proxy
        self.non_special_proxy_history[get_non_specialized_string(original)] = get_non_specialized_string(proxy)

        return proxy

    def get_proxy_from_original_non_special(self, string):
        splitted = string.split('.')
        findee = splitted[0]
        ext = splitted[1]
        if findee in self.non_special_proxy_history:
            return self.non_special_proxy_history[findee] + '.' + ext
        return

    def get_original_from_proxy_non_special(self, string):
        findee = string.split('.')[0]
        for original, proxy in self.non_special_proxy_history.items():
            if proxy == findee:
                return original + '.' + string.split('.')[1]
        return

    def is_proxy_or_original(self, string):
        # detect if a file is proxified, original or unrelated
        if "/" in string:
            if string in self.proxy_history.keys():
                return "original"
            elif string in self.proxy_history.values():
                return "proxy"
            return "irrelevant"
        else:
            if (string.split('.'))[0] in self.non_special_proxy_history.keys():
                return "original"
            elif (string.split('.'))[0] in self.non_special_proxy_history.values():
                return "proxy"
            return "irrelevant"

    def proxify_mod_files_in_folder(self, folder_path, is_root, is_revert):

        files_to_be_proxified = []

        if is_root:

            files_to_be_proxified = self.proxify_mod_files_in_folder(folder_path, False, is_revert)

            file_count = len(files_to_be_proxified)
            cur_file = 0
            if is_revert:
                print_localized("reverting_old_version_proxies")
            else:
                print_localized("changing_url")

            for file in files_to_be_proxified:
                original_modify_time = os.path.getmtime(file)  # capture modify time

                self.proxify_file(file,is_revert)

                os.utime(file, (original_modify_time, original_modify_time))  # restore modify time

                cur_file += 1
                done = int(50 * cur_file / file_count)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                sys.stdout.flush()
            print()

        else:
            # Replace blocked links with proxy links inside json files
            # (without changing modify time so it wont change the order of mods inside game)
            json_files = [pos_json for pos_json in os.listdir(folder_path) if pos_json.endswith('.json')]
            for file_name in json_files:
                files_to_be_proxified.append(folder_path + file_name)

            # recursively proxify sub folders
            sub_folders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
            for sub_folder in sub_folders:
                files_to_be_proxified += self.proxify_mod_files_in_folder(sub_folder + "\\", False, is_revert)

            return files_to_be_proxified

        return

    def proxify_file(self, file_path, is_revert):
        s = None

        with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
            s = f.read()

        if not is_revert:
            proxiable_list = self.url_expression.findall(s)
            if len(proxiable_list) > 0:
                for r in proxiable_list:
                    sliced = r[0][1:-1]
                    self.calculate_proxy(sliced)
            else:
                return

        for original, proxy in self.proxy_history.items():
            if not is_revert:
                s = s.replace(original, proxy)
            else:
                s = s.replace(proxy, original)

        with open(file_path, 'w', encoding='utf8') as f:
            f.write(s)
        return

    def reset_proxy_history(self, file_path):
        self.proxy_history = {}
        self.non_special_proxy_history = {}
        os.remove(file_path)

    def save_proxy_history(self, file_path):
        print(get_localized_string("saving_proxy_history") + file_path)
        s = json.dumps(
            {
                "proxy_history": self.proxy_history,
                "non_special_proxy_history": self.non_special_proxy_history}
            ,indent=4, separators=(',', ': '))

        with open(file_path, 'w', encoding='utf8') as f:
            f.write(s)

        return

    def load_proxy_history(self, file_path):
        print(get_localized_string("loading_proxy_history") + file_path)
        if not os.path.isfile(file_path):
            print_localized("history_not_found")
            return

        s = None
        with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
            s = f.read()
        j = json.loads(s)
        self.proxy_history = j["proxy_history"]
        self.non_special_proxy_history = j["non_special_proxy_history"]
        return
