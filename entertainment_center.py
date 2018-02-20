import fresh_tomatoes
import media
import json

# The name of the movies data file
MOVIE_DATA_FILE = "movies.json"


def json_to_dic():
    """
    This function will read json file which stores movie data and transfer it to a dictionary

    Args:
        none

    Returns:
        movie_data: dictionary stores movie data
    """
    file = open(MOVIE_DATA_FILE, 'r')
    movie_data = json.loads(file.read())
    file.close()
    return movie_data


def create_movie_objects(movie_data):
    """
    This function create the movie object and stores it to a list

    Args:
        none

    Returns:
        movie_objects: a list that contains movie objects
    """
    movie_objects = []
    for m in movie_data:
        movie = media.Movie(m)
        movie_objects.append(movie)
    return movie_objects

# Beginning of the program
fresh_tomatoes.open_movies_page(create_movie_objects(json_to_dic()))
