

class Grid:
    def __init__(self, max_longitude, min_longitude, max_latitude, min_latitude):
        self.max_longitude = max_longitude
        self.min_longitude = min_longitude
        self.max_latitude = max_latitude
        self.min_latitude = min_latitude

    def contains(self, coordinate):
        (longitude, latitude) = coordinate
        if (self.min_longitude < longitude <= self.max_longitude and
                self.min_latitude < latitude <= self.max_latitude):
            return True
        else:
            return False


