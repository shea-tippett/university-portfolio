"""
File: robot.py
Description: A program that creates different robots based on personality traits.
These robots have a model, tier and performance (which is calculated based on individual robots).
Author: Shea Tippett
"""

from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, model: str, tier: str):
        self.__model = model
        self.__tier = tier
        self.__performance = 5
        self.__upgrades = []
    
    def get_model(self):
        return self.__model
    
    def get_tier(self):
        return self.__tier
    
    def get_performance(self):
        return self.__performance
    
    def get_upgrades(self):
        return self.__upgrades
    
    def set_performance(self, performance):
        self.__performance = performance

    def install_upgrade(self, upgrade):
        self.__upgrades.append(upgrade)
        upgrade.apply(self)

    def __str__(self):
        upgrades_str = ", ".join(type(upgrade).__name__ for upgrade in self.__upgrades)
        return (
            f"{self.get_tier()} Robot - Model: {self.get_model()}, "
            f"Performance: {self.get_performance()}\n"
            f"Upgrades: {upgrades_str if upgrades_str else 'None'}"
        )
    
    @abstractmethod
    def execute_task(self):
        pass




