import json
import mmap

from sydGrid import Grid

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

grids = []
f1 = open("sydGrid.json")
grid_info = json.load(f1)
for area in grid_info["features"]:
    max_longitude = float("-inf")
    min_longitude = float("inf")
    max_latitude = float("-inf")
    min_latitude = float("inf")
    lst_coordinates = area["geometry"]["coordinates"][0]
    for coordinates in lst_coordinates:
        [longitude, latitude] = coordinates
        max_longitude = max(max_longitude, longitude)
        min_longitude = min(min_longitude, longitude)
        max_latitude = max(max_latitude, latitude)
        min_latitude = min(min_latitude, latitude)
    grid = Grid(max_longitude, min_longitude, max_latitude, min_latitude)
    grids.append(grid)




