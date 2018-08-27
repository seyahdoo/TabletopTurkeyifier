from main import version
import os

s = ""

with open("version_file.txt", 'r', encoding='utf8', errors='ignore') as f:
    s = f.read()


version_edited = version + ".0"
s = s.replace("x.x.x.x", version_edited)

version_edited = version_edited.replace(".", ",")
s = s.replace("x,x,x,x", version_edited)

with open("version_file_created.txt", 'w', encoding='utf8') as f:
    f.write(s)

os.system("pyinstaller --onefile main.py --version-file=\"version_file_created.txt\"")

os.remove("version_file_created.txt")

filename = "./dist/tabletop-turkeyifier-"
filename += version
filename += ".exe"

if os.path.isfile(filename):
    os.remove(filename)

os.rename("./dist/main.exe", filename)
