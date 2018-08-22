import requests
import json
import os
from sys import exit

from util import download_with_progress
from localization import print_localized


def update_app(current_version):

    # Get latest release
    r = requests.get('https://api.github.com/repos/seyahdoo/TabletopTurkeyifier/releases/latest')
    if r.ok:
        latest_release = json.loads(r.text or r.content)
        if latest_release["tag_name"] > current_version:
            print_localized("updating")
            for asset in latest_release["assets"]:
                download_with_progress(asset["browser_download_url"], asset["name"])
                print_localized("starting_new_version")
                os.startfile(asset["name"])
                exit(0)
        else:
            # Delete old versions if exists in same folder
            for filename in os.listdir():
                if filename.startswith("tabletop-turkeyifier-"):
                    if filename[-9:-4] < current_version:
                        print_localized("deleting_old_ver")
                        with open(filename, 'w'):
                            pass
                        os.remove(filename)
    return
