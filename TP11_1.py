import urllib.parse
import urllib.request
import json
from datetime import datetime
import sys

API_KEY = "YOUR_API_KEY"
NB_MAX_ACTORS = 6

if __name__ == '__main__':

    try:

        query = input("Search in movie database: ")
        parameters = urllib.parse.urlencode({"query": query, "api_key": API_KEY})
        print(parameters)

        response = urllib.request.urlopen(f"https://api.themoviedb.org/3/search/movie?{parameters}")
        results = json.load(response)

        for index, result in enumerate(results["results"]):
            if index + 1 > 5:
                break
            title = result["title"]

            try:

                release_date = datetime.datetime.strptime(result["release_date"], "%Y-%m-%d")
                year = str(release_date.year)

            except:
                year = "-"

            print(f"{index + 1}. {title} ({year})")

        index = input("? ")
        movie = results["results"][int(index) - 1]

        parameters = urllib.parse.urlencode({"api_key": API_KEY})
        response = urllib.request.urlopen(f"https://api.themoviedb.org/3/movie/{movie['id']}/credits?{parameters}")

        results = json.load(response)
        cast = ", ".join([f"{x['name']} (as {x['character']})" for x in results["cast"][:6]])

        print(f"{movie['title']} ({movie['release_date']}")
        print(f"With {cast}\n")
        print(f"Overview: {movie['overview']}")

        response = urllib.request.urlopen(f"https://image.tmdb.org/t/p/original{movie['poster_path']}")
        with open(f"{movie['title']}.jpg", "wb") as f:
            f.write(response.read())

    except Exception as e:
        print(e, file=sys.stderr)
