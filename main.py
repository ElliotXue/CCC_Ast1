import json
import mmap

from Utils import generate_grid

with open("smallTwitter.json", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    count = -1
    total_rows = 0
    offset = 0
    for line in iter(mm.readline, b""):
        str_line = line.decode().strip()
        if count == -1:
            str_line += "]}"
            head_row = json.loads(str_line)
            total_rows = head_row["total_rows"]
            # offset = head_row["offset"]
            total_rows = total_rows - offset

        elif count < total_rows-1:
            str_line = str_line[:-1]
            tweet = json.loads(str_line)

        elif count == total_rows-1:
            tweet = json.loads(str_line)

        count += 1

grids = generate_grid("sydGrid.json")


