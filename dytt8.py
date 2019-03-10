from bs4 import BeautifulSoup
from spider import Spider
from datetime import datetime
from urllib.parse import urlparse, urljoin


class Dytt8(Spider):
    def __init__(self):
        super().__init__(url="https://www.dytt8.net/html/gndy/dyzz/index.html")

    def parser(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        tables = soup.select('div.co_content8 table')
        results = []
        base_url = urlparse(self.url).netloc
        for mv in tables:
            title = mv.select('a.ulink')[0].text
            url = mv.select('a.ulink')[0].attrs['href']
            date = mv.find("font").text.split()[0][3:]
            film = dict(date=date, url=urljoin(self.url, url), title=title)
            if (self.now - datetime.strptime(date, "%Y-%m-%d")).days <= self.keep_days:
                results.append(film)

        return results

    def __call__(self):
        text = self.crawl(self.url)
        return self.parser(text)


if __name__ == "__main__":
    Dytt8()()
