import os


def print_size(size: int) -> str:
    sizes = ["B", "KB", "MB", "GB"]
    m = 0
    for i in range(len(sizes)):
        if size / (1024**i) < 1:
            break
        m = i
    return f"{round(size / (1024**m))}{sizes[m]}"


def get_size(path: str) -> int:
    size = 0
    os.chdir(f'{path}')
    for i in os.listdir():
        if os.path.isfile(i):
            size += os.path.getsize(i)
        if os.path.isdir(i):
            size += get_size(i)
    os.chdir(f'..')
    return size


def get_sizes() -> dict:
    sub = {}
    os.chdir('/home/asskicker54')
    for i in os.listdir():
        size = 0
        if os.path.isdir(i):
            size += get_size(i)
            sub[f'{i} {print_size(size)}'] = size
        if os.path.isfile(i):
            size = os.path.getsize(i)
            sub[f'{i} {print_size(size)}'] = size
    return sub


l = get_sizes()
l = sorted(l, key=l.get, reverse=True)
for i in l[:10]:
    print(i)
