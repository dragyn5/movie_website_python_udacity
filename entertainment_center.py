import fresh_tomatoes
import media

fight_club = media.Movie("fight Club", "A man's love hate relationship with himself", "https://images-na.ssl-images-amazon.com/images/I/71PwLE%2BJ3mL._SY550_.jpg", "https://www.youtube.com/watch?v=AZwsKVL6JfM" )



the_matrix = media.Movie("The Matrix", "A man discovers that the world is a simulation", "https://ih1.redbubble.net/image.12732159.3665/flat,550x550,075,f.u9.jpg", "https://www.youtube.com/watch?v=vKQi3bBA1y8")


groundhog_day = media.Movie("Goundhog Day", "A man relives the same day", "https://top100project.files.wordpress.com/2013/03/groundhog-day-3.jpg", "https://www.youtube.com/watch?v=tSVeDx9fk60")

hercules = media.Movie("Hercules", "A greek demigod goes on a quest to regain his godliness", "https://images-na.ssl-images-amazon.com/images/I/71QZf6eByiL._SY717_.jpg", "https://www.youtube.com/watch?v=ZvtspevZxpg")

movies = [fight_club ,the_matrix, groundhog_day, hercules]

fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.Valid_ratings)
