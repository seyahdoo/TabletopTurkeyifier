import json
import os

import requests
from localization import print_localized
from util import download_with_progress, get_file_properties
from version import version

latest_release = None


def get_latest_release():
    global latest_release

    # get latest release from cache
    if latest_release:
        return latest_release

    # get latest version from github api
    try:
        r = requests.get('https://api.github.com/repos/seyahdoo/TabletopTurkeyifier/releases/latest')
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print_localized("problem_checking_new_version")
        raise Exception("problem checking new version")

    if r.ok:
        # parse json api data
        latest_release = json.loads(r.text or r.content)
        return latest_release
    raise Exception("problem checking new version")


def update_app():

    # delete old updater if there is any
    for filename in os.listdir():
        props = get_file_properties(filename)
        app_name = None
        try:
            app_name = props["StringFileInfo"]["ProductName"]
        except:
            pass

        if app_name == "Tabletop Turkeyifier":
            if filename == "tabletop-turkeyifier-updater.exe":
                print_localized("deleting_updater")
                # wait for updater to close
                with open(filename, 'w'):
                    pass
                os.remove(filename)

    release = get_latest_release()

    # if there is a newer version or we are in production
    if release["tag_name"] != version and version != "development":
        print_localized("updating")

        # download updater,
        exec_name = None
        # download all it's assets
        for asset in release["assets"]:
            if asset["name"] is "tabletop-turkeyifier-updater.exe":
                download_with_progress(asset["browser_download_url"], asset["name"])
                exec_name = asset["name"]

        # start new version and exit program
        if exec_name is not None:
            print_localized("starting_updater")
            os.startfile(exec_name)
            exit(0)
        else:
            print_localized("problem_downloading_new_ver")
    return


if __name__ == "__main__":

    # Delete old versions if exists in same folder
    for filename in os.listdir():
        props = get_file_properties(filename)
        app_name = None
        try:
            app_name = props["StringFileInfo"]["ProductName"]
        except:
            pass

        prod_ver = None
        try:
            prod_ver = props["StringFileInfo"]["ProductVersion"]
        except:
            pass

        if app_name == "Tabletop Turkeyifier":
            if prod_ver is not None:
                if prod_ver < version:
                    print_localized("deleting_old_ver")
                    # wait for old version to close
                    with open(filename, 'w'):
                        pass
                    os.remove(filename)

    # download new version
    release = get_latest_release()

    exec_name = None
    # download executable
    for asset in release["assets"]:
        if asset["name"] is "tabletop-turkeyifier.exe":
            download_with_progress(asset["browser_download_url"], asset["name"])
            exec_name = asset["name"]

    # open new version
    if exec_name is not None:
        print_localized("starting_new_version")
        os.startfile(exec_name)
        exit(0)

