"""
File: sniper_robot.py
Description: A sniper robot that aims a sniper and calculates the performance
based on the weapon charge and stability.
Author: Shea Tippett
"""

from robot import Robot

class SniperRobot(Robot):
    def __init__(self, model, tier, weapon_charge: float, stability: float):
        super().__init__(model, tier)
        self.__weapon_charge = weapon_charge
        self.__stability = stability
    

    def get_weapon_charge(self):
        return self.__weapon_charge
    
    def get_stability(self):
        return self.__stability
    
    def set_stability(self, stability):
        self.__stability = stability
    

    def calculate_performance(self):
        base_score = self.__weapon_charge + self.__stability
        
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
        print(f"{self.get_model()} is aiming for a precision long range shot.\n")

    
    def __str__(self):
        str_base = super().__str__()
        return (
            f"----- Sniper Robot -----\n"
            f"{str_base}\n"
            f"Weapon charge: {self.get_weapon_charge()}, Weapon stability: {self.get_stability()}\n"
            f"{"-"*40}"
        )
