from mrjob.job import MRJob

from urllib.request import urlopen
import uuid
import json

output_dir = "E:/ucheba/bi_data/second_task/json"

class JsonDownloader(MRJob):

    def mapper(self, _, line):
        response = urlopen(line)
        with open(f"{output_dir}/{uuid.uuid1()}.json", "wb") as file:
            file.write(response.read())
        yield  None, None


if __name__ == '__main__':
    JsonDownloader.run()