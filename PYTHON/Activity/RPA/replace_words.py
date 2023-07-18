import os

def find_file(filename):
    for file in os.listdir():
        if file == filename:
            return True
    return False

os.chdir('Activity/RPA/.txts')
result = False

while result == False:
    current_file = input("Source File: ")
    result = find_file(f"{current_file}.txt")

new_file = input("New File: ")
open(f"{new_file}.txt", "x")

message = open(f"{current_file}.txt", "r")
message = message.read()

replaced_word = input("Replaced Word: ").lower()
new_word = input("New Word: ").lower()

message = message.replace(replaced_word, new_word)

new_file = open(f"{new_file}.txt", "w")
new_file.write(message)

new_file.close()

