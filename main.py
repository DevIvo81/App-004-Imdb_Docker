import os
import random
import requests

from fake_useragent import UserAgent
from bs4 import BeautifulSoup


class MoviePicker:
    def __init__(self, url):
        self.url = url
        self.movies = {}
        self.fetch_and_store_data()

    def fetch_and_store_data(self):
        ua = UserAgent()
        headers = {'User-Agent': ua.random}

        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:

            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            movie_tags = soup.select("td.titleColumn")
            ratings = soup.select("td.ratingColumn.imdbRating > strong")

            for movie_tag, rating in zip(movie_tags, ratings):

                rating = float(rating.text)
                cast = movie_tag.a['title']

                tag = movie_tag.text.split()

                position = int(tag[0][: -1])
                year = tag[-1][1: -1]
                title = " ".join(tag[1: -1])

                self.movies[position] = {
                    "position": position,
                    "title": title,
                    "year": year,
                    "cast": cast,
                    "rating": rating,
                }
            return self.movies
        else:
            return "\nBad response!\n"

    def random_movie_suggestion(self):
        return self.movies[random.randint(1, 250)]


if __name__ == "__main__":

    os.system('cls')

    url = "https://www.imdb.com/chart/top"

    movies = MoviePicker(url)

    while True:

        input("\nPress ENTER for random movie suggestion\n")

        sugg = movies.random_movie_suggestion()
        print(sugg)

        if input("\nAnother suggestion? (Y/N) --> ").lower() == "n":
            print("\nFarewell...!\n")
            break
