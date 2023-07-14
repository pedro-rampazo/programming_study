import os
import re

def is_phone_number(phone_number):
    numbers = re.findall("[0-9]", phone_number)
    hifen = re.findall("[-]", phone_number)
    if len(numbers) == 8:
        if len(hifen) == 1:
            return True
    return False

os.chdir('RPA/Regex Project')

files = os.listdir()
files.sort()

for fls in files:
    print(f"{fls}\n")
    fls = open(fls, 'r')
    message = fls.read()
    
    for x in range(len(message)):
        gap = message[x:x+9]
        if is_phone_number(gap):
            print(f"Phone number found: {gap}")

    