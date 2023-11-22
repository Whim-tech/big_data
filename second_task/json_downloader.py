from mrjob.job import MRJob

import requests
import uuid
import json

output_dir = "E:/ucheba/bi_data/second_task/json"

class JsonDownloader(MRJob):

    def mapper(self, _, line):
        r = requests.get(line)
        data  = r.json()
        with open(f"{output_dir}/{uuid.uuid1()}.json", "w") as file:
            json.dump(data, file)
        yield  None, None


if __name__ == '__main__':
    JsonDownloader.run()