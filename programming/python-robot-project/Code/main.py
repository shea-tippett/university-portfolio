"""
File: main.py
Description: Instantiates robots and performs tasks for checking output.
Author: Shea Tippett
"""

from sniper_robot import SniperRobot
from perfectionist_robot import PerfectionistRobot
from music_robot import MusicRobot, MusicLibrary
from upgrades import TargetingLens, FashionChip, MemoryExpansion
from workshop import Workshop


# Create sniper robot
sniper = SniperRobot("HK-47", "Elite", 2.7, 0.6)
sniper.calculate_performance()  # Calculate initial performance

# Create perfectionist robot
perfectionist = PerfectionistRobot("PR-534R1", "Advanced", 1.5, True)
perfectionist.calculate_performance()  # Calculate initial performance

# Create music robot with a sample music library
library = [
    MusicLibrary("Random Access Memories", "Daft Punk", 8.7),
    MusicLibrary("To Pimp A Butterfly", "Kendrick Lamar", 9.6),
    MusicLibrary("In Rainbows", "Radiohead", 8.8)
]
music_bot = MusicRobot("MR-50U7", "Basic", library)
music_bot.calculate_performance()  # Calculate initial performance

# --- UPGRADE DEMONSTRATION ---

# Install TargetingLens on sniper
sniper.install_upgrade(TargetingLens())  # Improves weapon attributes

# Install FashionChip on perfectionist
perfectionist.install_upgrade(FashionChip())  # Enhances quality via design mode

# Install MemoryExpansion on music bot
music_bot.install_upgrade(MemoryExpansion())  # Improves performance from library

# --- WORKSHOP DEMONSTRATION ---

# Create workshop and add all robots
workshop = Workshop()
workshop.add_robot("S1", sniper)
workshop.add_robot("P1", perfectionist)
workshop.add_robot("M1", music_bot)

# Display full summary of all robots
print("\n--- FULL WORKSHOP SUMMARY ---")
workshop.summary()

# Filter robots by type
print("\n--- FILTER: Sniper Robots ---")
workshop.filter_by_type(SniperRobot)


# Sort robots by performance
print("\n--- SORTED BY PERFORMANCE ---")
workshop.sort_by_performance()


# Demonstrate robot functionality
print("\n--- EXECUTING TASKS ---")
sniper.execute_task()         # Should show aiming message
perfectionist.execute_task()  # Should show fashion selection
music_bot.execute_task()      # Should show memory lookup
