from mrjob.job import MRJob

from urllib.request import urlopen
import re

output_dir = "E:/ucheba/bi_data/second_task/json"

url_regex = r"https://rasp\.omgtu\.ru/api/schedule/person/(\d+)\?start=(\d\d\d\d\.\d\d\.\d\d)&finish=(\d\d\d\d\.\d\d\.\d\d)&lng=1"

def parse_url(url):
    result = re.search(url_regex, url)

    return result.group(1), result.group(2).replace(".", "-"), result.group(3).replace(".", "-")

class JsonDownloader(MRJob):

    def mapper(self, _, line):
        id, start, end = parse_url(line)
        response = urlopen(line)
        with open(f"{output_dir}/{id}_{start}_{end}.json", "wb") as file:
            file.write(response.read())
        yield  None, None


if __name__ == '__main__':
    JsonDownloader.run()