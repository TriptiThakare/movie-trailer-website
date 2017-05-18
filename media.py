# -*- coding: utf-8 -*-
"""
Created on Tue May 09 12:31:45 2017

@author: tripti.sharma
"""
import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""
## This function initializes the class variables 
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# This function opens the browser with the url given to the function
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
