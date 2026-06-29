"""
File: workshop.py
Description: A workshop that does various things like store the robots and assigns ID's,
installs upgrades and formats summaries and filters
Author: Shea Tippett
"""

class Workshop:
    def __init__(self):
        self.__robots = {}

    def add_robot(self, robot_id: str, robot):
        if robot_id in self.__robots:
            print(f"Robot ID '{robot_id}' already exists.")
        else:
            self.__robots[robot_id] = robot
    
    def install_upgrade(self, robot_id: str, upgrade):
        if robot_id in self.__robots:
            robot = self.__robots[robot_id]
            robot.install_upgrade(upgrade)
            print(f"Installed {type(upgrade).__name__} to robot {robot_id}")
        else:
            print(f"No robot found with ID '{robot_id}'.")
    
    def summary(self):
        print("\n--- Robot Summary ---")
        for robot_id, robot in self.__robots.items():
            robot_type = type(robot).__name__
            print(f"ID: {robot_id}")
            print(f"Type: {robot_type}")
            print(robot)
            print()
    
    def sort_by_performance(self):
        print("\n--- Robots Sorted by Performance ---")
        sorted_ids = self.__get_ids_sorted_by_performance()
        for robot_id in sorted_ids:
            robot = self.__robots[robot_id]
            print(f"ID: {robot_id}, Model: {robot.get_model()}, Score: {robot.get_performance()}")

    def filter_by_type(self, robot_class):
        print(f"\n--- Robots of Type {robot_class.__name__} ---")
        matching_ids = self.__get_ids_by_type(robot_class)
        for robot_id in matching_ids:
            robot = self.__robots[robot_id]
            print(f"ID: {robot_id}, Model: {robot.get_model()}, Score: {robot.get_performance()}")

    def __get_ids_sorted_by_performance(self):
        robot_items = list(self.__robots.items())
        for i in range(len(robot_items)):
            for j in range(i + 1, len(robot_items)):
                if robot_items[i][1].get_performance() < robot_items[j][1].get_performance():
                    robot_items[i], robot_items[j] = robot_items[j], robot_items[i]
        return [robot_id for robot_id, _ in robot_items]

    def __get_ids_by_type(self, robot_class):
        result = []
        for robot_id, robot in self.__robots.items():
            if isinstance(robot, robot_class):
                result.append(robot_id)
        return result