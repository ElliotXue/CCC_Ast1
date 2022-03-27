import json
import mmap

with open("tinyTwitter.json", "r+b") as f:
    lst = []
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    for line in iter(mm.readline, b""):
        str_line = line.decode().strip()
        lst.append(str_line)
    head_row = lst[0] + lst[-1]
    rest_lst = lst[1:-1]
    for row in rest_lst:
        new_row = row[:-1]
        obj = json.loads(new_row)

f1 = open("language.json")
language = json.load(f1)
print(language)
