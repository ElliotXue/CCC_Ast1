import json
import mmap
from Utils import generate_grid


class WorkUnit:
    def __init__(self, _id, total_cores, lang_file, grid_file):
        self.id = _id
        self.total_cores = total_cores
        f1 = open(lang_file)
        self.language_dict = json.load(f1)
        f1.close()
        self.grids = generate_grid(grid_file)

    def process_data(self, file):
        with open(file, "rb") as f:
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
                    offset = head_row["offset"]
                    total_rows = total_rows - offset
                elif count < total_rows - 1:
                    if count % self.total_cores == self.id:
                        str_line = str_line[:-1]
                        tweet = json.loads(str_line)
                        self.extract_data(tweet)

                elif count == total_rows - 1:
                    if count % self.total_cores == self.id:
                        tweet = json.loads(str_line)
                        self.extract_data(tweet)
                count += 1
        return self.grids

    def extract_data(self, tweet):
        coordinates = tweet["doc"]["coordinates"]
        lang = tweet["doc"]["lang"]
        if coordinates is not None and lang in self.language_dict.keys():
            point = coordinates["coordinates"]
            for grid in self.grids:
                if grid.contains(point):
                    grid.add_tweet(self.language_dict[lang])
