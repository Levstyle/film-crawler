from bs4 import BeautifulSoup
from spider import Spider
from datetime import datetime


class SeeHD(Spider):
    def __init__(self):
        super().__init__(url="http://www.seehd.so/thread-2")

    def parser(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        tds = soup.select('td.subject')
        results = []
        for td in tds:
            if td.select('i.icon_headtopic_3'): continue
            date = td.select('p.info span')[0].text
            title = td.select('p.title a')[-1].text
            url = td.select('p.title a')[-1].attrs['href']

            film = dict(date=date, url=url, title=title)

            if (self.now - datetime.strptime(date, "%Y-%m-%d")).days <= self.keep_days:
                results.append(film)

        return results


if __name__ == "__main__":
    SeeHD()()
