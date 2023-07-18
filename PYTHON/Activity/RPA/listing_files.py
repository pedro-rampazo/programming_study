import os

path = input("Path: ")

os.chdir(path)

for file in os.listdir():
    print(f"- {file} ({os.path.getsize(file)})")