import json
import mmap


class WorkUnit:
    def __init__(self, _id, total_cores, lang_file):
        self.id = _id
        self.total_cores = total_cores
        f1 = open(lang_file)
        self.language_dict = json.load(f1)
        self.result = {}

    def process_data(self, file):
        str_data = ""
        with open(file, "r+b") as f:
            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            for line in iter(mm.readline, b""):
                str_line = line.decode().strip()
                str_data += str_line
        dict_data = json.loads(str_data)
        total_rows = dict_data["total_rows"]
        tweet_lst = dict_data["rows"]
        for i in range(total_rows):
            if i%self.total_cores == self.id:
                tweet = tweet_lst[i]

    def extract_data(self, tweet):
        coordinates = tweet["doc"]["coordinates"]
        lang = tweet["doc"]["lang"]
        if coordinates is not None and lang in self.language_dict.keys():
            if







