import json
import urllib

from dotenv import load_dotenv
import json
import os
import urllib.request

load_dotenv('.env')
api_token: str = "Bearer " + os.getenv('API_TOKEN')
api_key: str = os.getenv('API_KEY')

headers = {
    "accept": "application/json",
    "Authorization": api_token
}


def get_movie_list(page: int, list_type: str = "now_playing"):
    url = f"https://api.themoviedb.org/3/movie/{list_type}?api_key={os.getenv('API_KEY')}&page={page}"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return dict["results"]


def get_movie(movie_id: int):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={os.getenv('API_KEY')}"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return dict


if __name__ == "__main__":
    get_movie(709631)
