from seehd import SeeHD
from dytt8 import Dytt8
from prettytable import PrettyTable


def main():
    movies = PrettyTable(["电影名", "地址", "时间"])
    movies.align["电影名"] = "l"
    movies.align["地址"] = "c"
    movies.align["时间"] = "c"

    for movie in SeeHD()() + Dytt8()():
        movies.add_row([movie['title'], movie['url'], movie['date']])
    print(movies.get_string(sortby='时间', reversesort=True))


if __name__ == '__main__':
    main()
