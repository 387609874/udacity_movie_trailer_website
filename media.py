class Movie(object):
    """docstring for Movie"""

    def __init__(self, movie):
        """
        Constructor of this class
        """
        self.title = movie["title"]
        self.storyline = movie["storyline"]
        self.poster_image_url = movie["poster_image_url"]
        self.trailer_youtube_url = movie["trailer_youtube_url"]

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
