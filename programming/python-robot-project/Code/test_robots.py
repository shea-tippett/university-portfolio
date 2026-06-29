"""
File: test_robots.py
Description: Performs various tests for robots and functionality, currenly coverage
is at 94%.
Author: Shea Tippett
"""

from sniper_robot import SniperRobot
from perfectionist_robot import PerfectionistRobot
from music_robot import MusicRobot, MusicLibrary
from upgrades import TargetingLens, FashionChip, MemoryExpansion

# sniper robot tests
def test_sniper_robot_performance_basic():
    bot = SniperRobot("S-101", "Basic", 2.0, 1.0)
    bot.calculate_performance()
    expected = (2.0 + 1.0) * 1.5
    assert bot.get_performance() == expected

def test_sniper_robot_performance_elite():
    bot = SniperRobot("S-9000", "Elite", 3.5, 0.5)
    bot.calculate_performance()
    expected = (3.5 + 0.5) * 4.6
    assert bot.get_performance() == expected

def test_robot_str_output_sniper():
    bot = SniperRobot("S-TSTR", "Basic", 1.0, 1.0)
    output = str(bot)
    assert "Model: S-TSTR" in output
    assert "Basic Robot" in output
    assert "Weapon charge: 1.0" in output
    assert "Weapon stability: 1.0" in output

#perfectionist robot tests
def test_perfectionist_focus_mode_on():
    bot = PerfectionistRobot("P-Alpha", "Advanced", 2.0, True)
    bot.calculate_performance()
    expected = round((2.0 + 4.0) * 2.8, 2)
    assert bot.get_performance() == expected

def test_perfectionist_focus_mode_off():
    bot = PerfectionistRobot("P-Beta", "Advanced", 2.0, False)
    bot.calculate_performance()
    expected = round(2.0 * 2.8, 2)
    assert bot.get_performance() == expected

# music robot tests
def test_music_robot_performance():
    albums = [
        MusicLibrary("A", "Artist A", 8.0),
        MusicLibrary("B", "Artist B", 9.0),
        MusicLibrary("C", "Artist C", 10.0)
    ]
    bot = MusicRobot("M-001", "Elite", albums)
    bot.calculate_performance()
    avg = (8.0 + 9.0 + 10.0) / 3
    expected = avg * 4.6
    assert round(bot.get_performance(), 2) == round(expected, 2)

def test_robot_str_output_music():
    albums = [MusicLibrary("T", "Artist", 9.0)]
    bot = MusicRobot("M-TSTR", "Basic", albums)
    output = str(bot)
    assert "Music Library:" in output

def test_music_library_str():
    album = MusicLibrary("Hybrid Theory", "Linkin Park", 9.2)
    result = str(album)
    assert "Hybrid Theory" in result
    assert "Linkin Park" in result

# upgrade tests
def test_targeting_lens_upgrade():
    bot = SniperRobot("X-99", "Advanced", 2.0, 1.0)
    bot.calculate_performance()
    original = bot.get_performance()
    bot.install_upgrade(TargetingLens())
    assert bot.get_performance() > original

def test_fashion_chip_upgrade():
    bot = PerfectionistRobot("P-F", "Basic", 1.5, True)
    bot.calculate_performance()
    original = bot.get_performance()
    bot.install_upgrade(FashionChip())
    assert bot.get_performance() > original

def test_memory_expansion_upgrade():
    albums = [
        MusicLibrary("X", "Y", 7.5),
        MusicLibrary("Z", "W", 8.5)
    ]
    bot = MusicRobot("M-Z", "Basic", albums)
    bot.calculate_performance()
    original = bot.get_performance()
    bot.install_upgrade(MemoryExpansion())
    assert bot.get_performance() > original

def test_multiple_upgrades():
    bot = SniperRobot("X-MULTI", "Advanced", 1.0, 1.0)
    bot.calculate_performance()
    original = bot.get_performance()
    bot.install_upgrade(TargetingLens())
    bot.install_upgrade(TargetingLens())
    assert bot.get_performance() > original

def test_upgrade_string_repr():
    upgrade = FashionChip()
    assert isinstance(str(upgrade), str)
    assert "FashionChip" in str(upgrade)

# edge cases
def test_perfectionist_robot_invalid_tier():
    bot = PerfectionistRobot("PR-WTF", "Super", 1.0, False)
    bot.calculate_performance()
    # No multiplier
    assert bot.get_performance() == 1.0

def test_music_robot_empty_library():
    bot = MusicRobot("MR-NULL", "Basic", [])
    bot.calculate_performance()
    assert bot.get_performance() == 0