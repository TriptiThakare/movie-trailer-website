# -*- coding: utf-8 -*-
"""
Created on Tue May 09 12:38:29 2017

@author: tripti.sharma
"""
import media
import fresh_tomatoes

# list of movies to be displayed
movies = [media.Movie("Kal Ho Naa Ho",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/b/b4/KalHoNaaHo.jpg/220px-KalHoNaaHo.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=tVMAQAsjsOU"),
          media.Movie("Dilwale Dulhania Le Jayenge",
                      "https://upload.wikimedia.org/wikipedia/en/8/80/Dilwale_Dulhania_Le_Jayenge_poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=c25GKl5VNeY"),
          media.Movie("Toy Story",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc"),
          media.Movie("Dangal",
                      "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=x_7YlGv9u1g"),
          media.Movie("School of Rock",
                      "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=XCwy6lW5Ixc"),
          media.Movie("Ratatouille",
                      "http://www.pixartalk.com/wp-content/uploads/2009/06/ratrussian1.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=c3sBBRxDAqk"),
          media.Movie("Midnight in Paris",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/220px-Midnight_in_Paris_Poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=FAfR8omt-CY"),
          media.Movie("Avatar",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY"),
          media.Movie("Hunger Games",
                      "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=mfmrPu43DF8")]

# create html page displaying the list of movies
fresh_tomatoes.open_movies_page(movies)
