import requests
from datetime import datetime
import asyncio


class Spider:
    def __init__(self, url, keep_days=10):
        self.url = url
        self.keep_days = keep_days
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive"
        }
        self.requests = requests.Session()
        self.requests.headers.update(self.headers)
        self.now = datetime.now()

    def crawl(self, url):
        response = self.requests.get(url=url)
        response.encoding = response.apparent_encoding
        return response.text

    def parser(self):
        pass

    @asyncio.coroutine
    def __call__(self):
        result = self.parser(self.crawl(self.url))
        print("{} is done!".format(self.url))
        return result
