import json

from Grid import Grid


def generate_grid(file):
    grids = []
    f1 = open(file)
    grid_info = json.load(f1)
    for area in grid_info["features"]:
        max_longitude = float("-inf")
        min_longitude = float("inf")
        max_latitude = float("-inf")
        min_latitude = float("inf")
        lst_coordinates = area["geometry"]["coordinates"][0]
        id = area["properties"]["id"]
        for coordinates in lst_coordinates:
            [longitude, latitude] = coordinates
            max_longitude = max(max_longitude, longitude)
            min_longitude = min(min_longitude, longitude)
            max_latitude = max(max_latitude, latitude)
            min_latitude = min(min_latitude, latitude)
        grid = Grid(max_longitude, min_longitude, max_latitude, min_latitude, id)
        grids.append(grid)
    grids = sorted(grids, key=lambda x: (-x.center_point[1], x.center_point[0]))
    count = 0
    for letter in "ABCD":
        for num in range(1, 5):
            grids[count].cell_name = letter + str(num)
            count += 1
    f1.close()
    return grids


def integration(grids_1, grids_2):
    for i in range(len(grids_1)):
        grids_1[i].combine(grids_2[i])
