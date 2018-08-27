from main import version
import os

s = ""

with open("version_file.txt", 'r', encoding='utf8', errors='ignore') as f:
    s = f.read()

version = version + ".0"
s = s.replace("x.x.x.x", version)

version = version.replace(".",",")
s = s.replace("x,x,x,x", version)

with open("version_file_created.txt", 'w', encoding='utf8') as f:
    f.write(s)

os.system("pyinstaller --onefile main.py --version-file=\"version_file_created.txt\"")

os.remove("version_file_created.txt")

if os.path.isfile("./dist/tabletop-turkeyifier.exe"):
    os.remove("./dist/tabletop-turkeyifier.exe")

os.rename("./dist/main.exe","./dist/tabletop-turkeyifier.exe")
