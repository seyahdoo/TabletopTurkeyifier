from main import version
import os

s = ""

with open("build_properties_template.txt", 'r', encoding='utf8', errors='ignore') as f:
    s = f.read()

version_edited = version
s = s.replace("x.x.x.x", version_edited)

with open("tmp_build_properties.txt", 'w', encoding='utf8') as f:
    f.write(s)

os.system("pyinstaller --onefile main.py --version-file=\"tmp_build_properties.txt\"")

os.remove("tmp_build_properties.txt")

filename = "./dist/tabletop-turkeyifier.exe"

if os.path.isfile(filename):
    os.remove(filename)

os.rename("./dist/main.exe", filename)
