import os

os.makedirs('./activity/Backup Zip/files')
current_path = os.path.join('activity', 'Backup Zip', 'files')
os.chdir(current_path)

for f in range(20):
    file = open(f'file#{f+1}.txt', 'w')
    file.write(f'This is my file number #{f+1}')
    file.close()

