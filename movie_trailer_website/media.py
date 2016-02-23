import webbrowser


class Movie:
    # The constructor for the Movie class to initialize the values.
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 movie_poster_image_url,
                 movie_trailer_youtube_url):
        # Assign values to the Movie class variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url

    # This method opens the link in a browser for the selected movie's trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


