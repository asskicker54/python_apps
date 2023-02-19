import os
from zipfile import ZipFile
import json
import shutil

with ZipFile('arc.zip') as myzip:
    myzip.extractall('./zip')
    os.chdir(f'zip')
    count = 0
    for cur_dir, dirs, files in os.walk('.'):
        size = 0
        for i in files:
            try:
                with open(os.path.join(cur_dir, i)) as json_file:
                    f = json.load(json_file)
                    if f["city"] == "Moscow":
                        count += 1
            except:
                print("No such files")
    print(count)
os.chdir('..')
shutil.rmtree("zip")
