from bs4 import BeautifulSoup
from spider import Spider
from datetime import datetime
from urllib.parse import urljoin


class PiaoHua(Spider):
    def __init__(self):
        super().__init__(url="https://www.piaohua.com/html/dianying.html")

    def parser(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        uls = soup.select('ul.ul-imgtxt1')[0].select('li')

        results = []
        for ul in uls:
            url = urljoin(self.url, ul.find('a').attrs['href'])
            title = ul.select('div.txt>h3')[0].text
            date = ul.select('span')[0].text

            film = dict(date=date, url=url, title=title)

            if (self.now - datetime.strptime(date, "%Y-%m-%d")).days <= self.keep_days:
                results.append(film)

        return results


if __name__ == "__main__":
    piaohua = PiaoHua()
    piaohua.parser(piaohua.crawl(piaohua.url))
