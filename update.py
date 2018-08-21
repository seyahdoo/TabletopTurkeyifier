import requests
import json
import os
import time

from util import download_with_progress


def self_update(version):

    r = requests.get('https://api.github.com/repos/seyahdoo/TabletopTurkeyifier/releases/latest')
    if r.ok:
        latest = json.loads(r.text or r.content)
        if latest["tag_name"] > version:
            print("Updating")
            for asset in latest["assets"]:
                print("Downloading assets")
                print(asset["browser_download_url"])
                download_with_progress(asset["browser_download_url"],asset["name"])
                print("Starting new version: " + asset["name"])
                os.startfile(asset["name"])
                exit(0)
        else:
            # Delete old versions
            for filename in os.listdir():
                if filename.startswith("tabletop-turkeyifier-"):
                    if filename[-9:-4] < version:
                        time.sleep(1) # let it close
                        os.remove(filename)
    return
