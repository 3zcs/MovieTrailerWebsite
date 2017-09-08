import webbrowser


''' Movie class show each movie object '''
class Movie:
    valid_ratings = ["G", "PG", "PG-13", "R"]
    ''' constractur method take title, storyline, poster and trailer '''
    def __init__(self, movie_title, movie_storyline,
                 movie_poster_image, movie_trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_youtube

    ''' show_trailer method return a trailer '''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

