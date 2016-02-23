import fresh_tomatoes
import media

# Instantiate objects of Movie class with different values.
swades = media.Movie("Swades",
    "A successful Indian scientist returns to an Indian village to take his "
    "nanny to America with him and in the process rediscovers his roots.",
    "https://upload.wikimedia.org/wikipedia/en/5/5f/Swades_movie_poster.png",
    "https://www.youtube.com/watch?v=y95DpoSP7i0")

kal_ho_naa_ho = media.Movie("Kal Ho Naa Ho",
    "The story of a dying man who lived forever",
    "https://upload.wikimedia.org/wikipedia/en/b/b4/KalHoNaaHo.jpg",
    "https://www.youtube.com/watch?v=r--TDwkNBdM")

titanic = media.Movie("Titanic",
    "American epic romantic disaster with the sinking of the RMS Titanic",
    "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
    "www.youtube.com/watch?v=2e-eXJ6HgkQ")

pursuit_of_happiness = media.Movie("Pursuit of Happyness",
    "American biographical drama film based on Chris Gardner's nearly one-year "
    "struggle being homeless",
    "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
    "https://www.youtube.com/watch?v=89Kq8SDyvfg")

a_beautiful_mind = media.Movie("A Beautiful Mind",
    "American biographical drama film based on the life of John Nash, a Nobel "
    "Laureate in Economics",
    "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
    "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

october_sky = media.Movie("October Sky",
    "Based on the true story of Homer H. Hickam, Jr., a coal miner's son who "
    "eventually became a NASA engineer",
    "https://upload.wikimedia.org/wikipedia/en/7/73/October_sky_poster.jpg",
    "https://www.youtube.com/watch?v=zxJQgYPXjN4")

# Create a list of Movie objects instantiated above.
movies_list = [swades,
               titanic,
               kal_ho_naa_ho,
               october_sky,
               a_beautiful_mind,
               pursuit_of_happiness]

# Open the movies page in a web browser.
fresh_tomatoes.open_movies_page(movies_list)
