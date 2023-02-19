import os

files = os.listdir('./')
print(files)

for file in files:
    if "." in file:
        file_size = os.path.getsize(file)
        if file_size >= 1024:
            print(f"{file} {file_size // 1024}KB")
        elif file_size >= 1024 * 1024:
            print(f"{file} {file_size // (1024 * 1024)}MB")
        else:
            print(f"{file} {file_size}B")
