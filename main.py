from seehd import SeeHD
from prettytable import PrettyTable


def main():
    movies = PrettyTable(["电影名", "地址", "时间"])
    movies.align["电影名"] = "l"
    movies.align["地址"] = "c"
    movies.align["时间"] = "c"
    movies.sortby = "时间"

    for movie in SeeHD()():
        movies.add_row([movie['title'], movie['url'], movie['date']])
    print(movies)


if __name__ == '__main__':
    main()
