"""
File: music_robot.py
Description: A music robot that contains a list of albums and calculates performance
based on the total of the metacritic ratings associated with the albums.
Author: Shea Tippett
"""

from robot import Robot

class MusicLibrary:
    def __init__(self, album_title: str, artist: str, metacritic_rating: float):
        self.__album_title = album_title
        self.__artist = artist
        self.__metacritic_rating = metacritic_rating
    
    def get_album_title(self):
        return self.__album_title
    
    def get_artist(self):
        return self.__artist
    
    def get_metacritic_rating(self):
        return self.__metacritic_rating
    

    def __str__(self):
        return f"Album: {self.__album_title}, Artist: {self.__artist}, Metacritic Rating: {self.__metacritic_rating}"


class MusicRobot(Robot):
    def __init__(self, model, tier, music_library: list["MusicLibrary"]):
            super().__init__(model, tier)
            self.__music_library = music_library
        
    def get_music_library(self):
        return self.__music_library
    

    def calculate_performance(self):
        ratings = [music.get_metacritic_rating() for music in self.get_music_library()]
        
        if not ratings:
            base_score = 0
        else:
            base_score = sum(ratings) / len(ratings)
        
        tier = self.get_tier().lower()
        if tier == "basic":
            performance = base_score * 1.5
        elif tier == "advanced":
            performance = base_score * 2.8
        elif tier == "elite":
            performance = base_score * 4.6
        else:
            performance = base_score
        
        self.set_performance(performance)


    def execute_task(self):
        print(f"{self.get_model()} is flipping through memory for 3 best albums.\n")


    def __str__(self):
        str_base = super().__str__()
        music_entries = "\n".join(str(music) for music in self.get_music_library())
        return (
            f"----- Music Robot -----\n"
            f"{str_base}\n"
            f"Music Library:\n"
            f"{music_entries}\n"
            f"{"-"*40}"
        )
        
        