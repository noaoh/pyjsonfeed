import os
from pyjsonfeed import pyjsonfeed
import unittest
import json
import html

url_prefix = "https://gist.githubusercontent.com/noaoh/4c7f40153ec58f462e437f90b5b49f25/raw/2d0814f2f84a7c005bc0589f48692b7b25ecedf8/"
urls = sorted([url_prefix + x for x in ['jsonfeed_feed.json', 'npr_feed.json', 'flyingmeat_feed.json']])
files = []
feeds = []
strings = []

os.chdir(os.path.dirname(__file__))
for feed in sorted(os.listdir("feeds")):
    if feed.endswith(".json") and "output" not in feed:
        with open("feeds/" + feed) as f:
            json_data = json.load(f)
            feeds.append(json_data)
            strings.append(json.dumps(json_data))

        files.append("feeds/" + feed)

files = sorted(files)

class TestParseMethod(unittest.TestCase):
    def test_url(self):
        for actual, expected in zip(urls, feeds[0:3]):
            with self.subTest():
                self.assertEqual(pyjsonfeed.parse(actual)._asdict(), expected)


    def test_file(self):
        for actual, expected in zip(files, feeds):
            with self.subTest():
                self.assertEqual(pyjsonfeed.parse(actual)._asdict(), expected)


    def test_string(self):
        for actual, expected in zip(strings, feeds):
            with self.subTest():
                self.assertEqual(pyjsonfeed.parse(actual)._asdict(), expected)


if __name__ == "__main__":
    unittest.main()

