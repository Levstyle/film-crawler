from seehd import SeeHD
from dytt8 import Dytt8
from piaohua import PiaoHua
from prettytable import PrettyTable
from functools import reduce
import asyncio


def main():
    movies = PrettyTable(["电影名", "地址", "时间"])
    movies.align["电影名"] = "l"
    movies.align["地址"] = "c"
    movies.align["时间"] = "c"

    tasks = [
        asyncio.ensure_future(SeeHD()()),
        asyncio.ensure_future(Dytt8()()),
        asyncio.ensure_future(PiaoHua()())
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    films = reduce(lambda x, y: x + y, [task.result() for task in tasks])
    for movie in films:
        movies.add_row([movie['title'], movie['url'], movie['date']])

    print(movies.get_string(sortby='时间', reversesort=True))

    loop.close()


if __name__ == '__main__':
    main()
