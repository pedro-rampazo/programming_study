import os
import re

def find_file(filename):
    files = os.listdir()
    for f in files:
        if f == filename:
            return True
    return False

def clear_message(message):
    caracters = re.findall("[?!,.]", message)
    for c in set(caracters):
        message = re.sub(re.escape(c), "", message)
    return message

def count_word(word, word_list):
    counter = 0
    for w in word_list:
        if w == word:
            counter += 1
    return counter

os.chdir('RPA/.txts')
filename = input('Filename: ')
filename = f"{filename}.txt"


if find_file(filename):
    fl = open(filename, 'r')
    message = fl.read()
    message = clear_message(message)
    message = message.split(" ")
    for m in set(message):
        word_times = count_word(m, message)
        print(f"{m}: {word_times} times")
    

