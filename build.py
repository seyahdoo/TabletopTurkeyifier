import os
import subprocess
from github import Github

cmd = subprocess.run(["git", "describe", "--abbrev=0"], stdout=subprocess.PIPE)
version: str = cmd.stdout.decode("utf-8")
version = version.strip()

with open("version.py", "w", encoding="utf8", errors="ignore") as f:
    f.write("version = \"{}\"".format(version))

print("::set-output name=version::{}".format(version))

properties_file_content = ""
with open("build_properties_template.txt", 'r', encoding='utf8', errors='ignore') as f:
    properties_file_content = f.read()
properties_file_content = properties_file_content.replace("x.x.x.x", version)
with open("tmp_build_properties.txt", 'w', encoding='utf8') as f:
    f.write(properties_file_content)

os.system("pyinstaller --onefile main.py --version-file=\"tmp_build_properties.txt\"")

os.remove("tmp_build_properties.txt")

filename = "./dist/tabletop-turkeyifier.exe"
if os.path.isfile(filename):
    os.remove(filename)
os.rename("./dist/main.exe", filename)



# GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
# g = Github(GITHUB_TOKEN)
#
# cmd = subprocess.run(["git", "config", "--get", "remote.origin.url"], stdout=subprocess.PIPE)
# repo_url: str = cmd.stdout.decode("utf-8")
# repo_url = repo_url.strip()
# print(repo_url)
#
# repo = g.get_repo(repo_url)
#
# release = repo.create_git_release(
#     version,
#     "Tabletop Turkeyifier {}".format(version),
#     "Tabletop Turkeyifier {}".format(version))









