import json
import mmap


with open("tinyTwitter.json", "r+b") as f:
    lst = []
    str1 = ""
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    for line in iter(mm.readline, b""):
        str_line = line.decode().strip()
        str1 += str_line
        lst.append(str_line)
    head_row = lst[0] + lst[-1]
    rest_lst = lst[1:-1]
    for row in rest_lst:
        new_row = row[:-1]
        obj = json.loads(new_row)

a = json.loads(str1)
print(id(a))
for i in a["rows"]:
    if i["doc"]["coordinates"] is not None:
        print(i["doc"]["coordinates"])







