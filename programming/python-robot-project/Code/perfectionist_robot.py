"""
File: perfectionist_robot.py
Description: A perfectionist robot that is very good at choosing an outfit and
stresses about everything, it calculates the performance based on quality level
and if focus mode is activated.
Author: Shea Tippett
"""

from robot import Robot

class PerfectionistRobot(Robot):
    def __init__(self, model, tier, quality_level: float, focus_mode: bool):
        super().__init__(model, tier)
        self.__quality_level = quality_level
        self.__focus_mode = focus_mode


    def get_quality_level(self):
        return self.__quality_level
    
    def set_quality_level(self, quality_level):
        self.__quality_level = quality_level
    
    def get_focus_mode(self):
        return self.__focus_mode
    
    def calculate_performance(self):
        base_score = self.__quality_level

        if self.__focus_mode:
            base_score += base_score * 2
        else:
            pass
        
        tier = self.get_tier().lower()
        if tier == "basic":
            performance = base_score * 1.5
        elif tier == "advanced":
            performance = base_score * 2.8
        elif tier == "elite":
            performance = base_score * 4.6
        else:
            performance = base_score
        
        performance = round(performance, 2)

        self.set_performance(performance)

    
    def execute_task(self):
        print(f"{self.get_model()} is charging computing power to choose outfit.\n")

    
    def __str__(self):
        str_base = super().__str__()
        return (
            f"----- Perfectionist Robot -----\n"
            f"{str_base}\n"
            f"Quality level: {self.get_quality_level()}, Focus mode activated: {self.get_focus_mode()}\n"
            f"{"-"*40}"
        )
