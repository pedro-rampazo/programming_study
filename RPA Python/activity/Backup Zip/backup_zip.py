import os
import zipfile

def designate_backup_name():
    counter = 1
    while True:
        filename = f'backup#{counter}'
        if filename not in os.listdir():
            return filename
        counter += 1

backups_path = os.path.join('activity', 'Backup Zip', 'backups')
os.chdir(backups_path)
filename = designate_backup_name()

new_zip = zipfile.ZipFile(filename, 'w')
os.chdir('../files')

for f in os.listdir():
    new_zip.write(f, compress_type=zipfile.ZIP_DEFLATED)

new_zip.close()

