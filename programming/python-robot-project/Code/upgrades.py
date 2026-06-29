"""
File: upgrades.py
Description: Creates various upgrades for each of the robots and applies them.
Author: Shea Tippett
"""

from abc import ABC, abstractmethod
from music_robot import MusicLibrary

class Upgrade(ABC):
    @abstractmethod
    def apply(self, robot):
        pass


class TargetingLens(Upgrade):
    def apply(self, robot):
        if hasattr(robot, "get_stability") and hasattr(robot, "set_stability"):
            current = robot.get_stability()
            robot.set_stability(current + 1.2)
        robot.calculate_performance()


class FashionChip(Upgrade):
    def apply(self, robot):
        if hasattr(robot, "get_quality_level") and hasattr(robot, "set_quality_level"):
            current = robot.get_quality_level()
            robot.set_quality_level(current + 2.0)
        robot.calculate_performance()


class MemoryExpansion(Upgrade):
    def apply(self, robot):
        if hasattr(robot, "get_music_library"):
            library = robot.get_music_library()
            library.append(MusicLibrary("Expanding Memeory", "In Robot", 9.9))
        robot.calculate_performance()