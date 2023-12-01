import json
import os
import urllib.request
from main import get_movie_list, get_movie

from flask import render_template, Flask

app = Flask(__name__)


@app.route("/")
def get_movies():
    movies = get_movie_list(1)
    return render_template("index.html", movies=movies)


@app.route("/popular")
def get_movies_popular():
    movies = get_movie_list(1, 'popular')
    return render_template("index.html", movies=movies)


@app.route("/top_rated")
def get_movies_top_rated():
    movies = get_movie_list(1, 'top_rated')
    return render_template("index.html", movies=movies)


@app.route("/upcoming")
def get_movies_upcoming():
    movies = get_movie_list(1, 'upcoming')
    return render_template("index.html", movies=movies)


@app.route("/movie/<movie_id>")
def movie(movie_id: int):
    movie_info = get_movie(movie_id)
    return render_template('movie.html', movie=movie_info)


app.run()
