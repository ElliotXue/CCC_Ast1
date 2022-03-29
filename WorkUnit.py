import json
import mmap


class WorkUnit:
    def __init__(self, _id, total_cores, lang_file):
        self.id = _id
        self.total_cores = total_cores
        f1 = open(lang_file)
        self.language_dict = json.load(f1)
        f1.close()
        self.result = {}

    def process_data(self, file):
        with open(file, "r+b") as f:
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
                    print(total_rows)
                elif count < total_rows-1:
                    str_line = str_line[:-1]
                    tweet = json.loads(str_line)

                elif count == total_rows-1:
                    tweet = json.loads(str_line)
                    print(tweet)
                count += 1


    def extract_data(self, tweet):
        coordinates = tweet["doc"]["coordinates"]
        lang = tweet["doc"]["lang"]
        if coordinates is not None and lang in self.language_dict.keys():
            if







