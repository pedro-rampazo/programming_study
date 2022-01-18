# open .txt
file = open('PYTHON/Theory/file_manipulation_text_files.txt')

# return BOOL value as verification if the file is open
print(file.closed)

# read .txt file
print(file.read())

# close file
file.closed()

# read a line
print(file.readline())

#---------------------------------------------------------------

# 'with' structure → open and close files
with open('PYTHON/Theory/file_manipulation_text_files.txt') as file:
    print(file.read())
    print(file.closed)
print(file.closed)