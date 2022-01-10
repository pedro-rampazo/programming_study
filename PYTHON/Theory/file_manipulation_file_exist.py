import os

# Return BOOL value. Indicate if a directory or file exists
print(os.path.exists('PYTHON/Theory/dictionary_01.py'))

# Create a new file
os.mknod('PYTHON/Theory/using_mknod.py')

# Create a new folder
os.mkdir('PYTHON/Theory/using_mkdir')

# Remove files
os.remove('PYTHON/Theory/using_mknod.py')

# Remove folder → It's only possible if the folder is EMPTY
os.rmdir('PYTHON/Theory/using_mkdir')

# Rename files and folder
os.rename('PYTHON/Theory/dictionary_01.py', 'PYTHON/Theory/dictionary.py')