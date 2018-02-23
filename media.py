import webbrowser
# Creates class for object instantiation
class Movie():
  VALID_RATINGS = ["PG-13", "R", "X", "XX", "XXX"]
# Initiation method
  def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube
# Method for showing youtube trailer
  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)