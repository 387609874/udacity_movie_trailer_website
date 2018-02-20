class Movie(object):
    """docstring for Movie"""

    # Define Movie Class
    def __init__(self, movie):
        """
        Constructor of this class. Movie class will store information relate
        to a movie such as title, storyline and etc.
        """
        self.title = movie["title"]
        self.storyline = movie["storyline"]
        self.poster_image_url = movie["poster_image_url"]
        self.trailer_youtube_url = movie["trailer_youtube_url"]

    def show_trailer(self):
        """
        This function will show open movie trailer url.
        """
        webbrowser.open(self.trailer_youtube_url)
