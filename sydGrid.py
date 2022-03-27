

class Grid:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def contains(self, coordinate):
        (longitude_coordinate, latitude_coordinate) = coordinate
        (longitude_top_left, latitude_top_left) = self.top_left
        (longitude_bottom_right, latitude_bottom_right) = self.bottom_right
        if (longitude_top_left < longitude_coordinate <= longitude_bottom_right and
                latitude_top_left <= latitude_coordinate < latitude_bottom_right):
            return True
        else:
            return False


