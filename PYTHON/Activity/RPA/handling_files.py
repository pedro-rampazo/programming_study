import os
import shutil

os.chdir("./Activity/RPA/.txts")

def change_filename():
    for n, f in enumerate(os.listdir()):
        os.rename(f, f"File {n}.txt")


def create_file():
    for f in range(100):
        open(f"file00{f}.txt", "x")

#change_filename()
create_file()
