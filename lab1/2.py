import os
from zipfile import ZipFile


def print_size(size: int) -> str:
    sizes = ["B", "KB", "MB", "GB"]
    m = 0
    for i in range(len(sizes)):
        if size / (1024**i) < 1:
            break
        m = i
    return f"{round(size / (1024**m))}{sizes[m]}"


with ZipFile('./archive.zip') as z:
    for name in z.namelist():
        items = name.rstrip("/").split("/")
        flag = False
        for i in items:
            if "." in i:
                flag = True
        if not flag:
            continue
        size = z.getinfo(name).file_size
        path = ""
        for i in range(len(items) - 1):
            path += " " + items[i]

        print(f"{path}    {items[-1]}    {print_size(size)}")
