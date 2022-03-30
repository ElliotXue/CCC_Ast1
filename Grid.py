

class Grid:
    def __init__(self, max_longitude, min_longitude, max_latitude, min_latitude, _id):
        self.cell_name = None
        self.max_longitude = max_longitude
        self.min_longitude = min_longitude
        self.max_latitude = max_latitude
        self.min_latitude = min_latitude
        self.id = _id
        self.center_point = ((max_longitude+min_longitude)/2, (max_latitude+min_latitude)/2)
        self.total_tweets = 0
        self.language_info = {}

    def contains(self, coordinate):
        (longitude, latitude) = coordinate
        if (self.min_longitude < longitude <= self.max_longitude and
                self.min_latitude < latitude <= self.max_latitude):
            return True
        else:
            return False

    def add_tweet(self, language):
        if language in self.language_info.keys():
            self.language_info[language] += 1
        else:
            self.language_info[language] = 1
        self.total_tweets += 1

    def combine(self, grid):
        for language in grid.language_info.keys():
            if language in self.language_info.keys():
                self.language_info[language] += grid.language_info[language]
            else:
                self.language_info[language] = grid.language_info[language]
        self.total_tweets += grid.total_tweets



