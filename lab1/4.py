import os
from zipfile import ZipFile
import datetime


def make_reserve_arc(source: str, dest: str) -> None:
    os.chdir(dest)
    date = str(datetime.datetime.now())
    with ZipFile('archive(' + date + ").zip", 'w') as myzip:
        os.chdir(source)
        for cur_dir, dirs, files in os.walk('.'):
            for file in files:
                myzip.write(os.path.join(cur_dir, file))


make_reserve_arc("./", "../archives")
