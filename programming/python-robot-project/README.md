# Python Robot Project

A small Python project that defines a set of robots with distinct personalities and capabilities. Each robot type calculates its performance differently and supports upgrade installation through a workshop interface.

## Project Structure

- `Code/`
  - `main.py` - Demonstrates robot creation, performance calculation, upgrades, and workshop features.
  - `robot.py` - Abstract base class for all robots.
  - `sniper_robot.py` - Robot subclass specializing in precision and weapon stability.
  - `perfectionist_robot.py` - Robot subclass focused on quality and focus mode.
  - `music_robot.py` - Robot subclass using a music library to calculate performance.
  - `upgrades.py` - Upgrade classes that modify robot attributes and recalculate performance.
  - `workshop.py` - Stores robots, installs upgrades, and prints summaries, filters, and sorted results.
  - `test_robots.py` - Test script for verifying robot behavior (current working file).

## Features

- Abstract `Robot` base class with performance tracking and upgrade support.
- Specialized robot types with custom performance formulas.
- Upgrade system for modifying robot capabilities at runtime.
- Workshop container for managing robots, filtering by type, and sorting by performance.

## Getting Started

1. Install Python 3.8 or newer.
2. Open a terminal in the `programming/python-robot-project/Code` directory.
3. Run the main demo:

```bash
python main.py
```

## Usage

- `main.py` shows robot instantiation, upgrade installation, and workshop operations.
- `test_robots.py` can be used to verify or extend automated tests.

## Notes

- Each robot must implement `execute_task()`.
- Upgrades call the robot's `calculate_performance()` after applying changes.
- The workshop can add robots, install upgrades by ID, print a summary, filter by class, and sort by performance.
