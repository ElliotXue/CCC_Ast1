import json

from sydGrid import Grid


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
        for coordinates in lst_coordinates:
            [longitude, latitude] = coordinates
            max_longitude = max(max_longitude, longitude)
            min_longitude = min(min_longitude, longitude)
            max_latitude = max(max_latitude, latitude)
            min_latitude = min(min_latitude, latitude)
        grid = Grid(max_longitude, min_longitude, max_latitude, min_latitude)
        grids.append(grid)
    return grids