import sqlite3
import datetime
from excercise_objects import Set, Exercise, Workout


CURRENTLY_IMPLEMENTED = 1
NUM_MENU_ITEMS = 7


def init_db():
    pass


def log_new_workout():
    # date = datetime.date.today()
    pass


CHOICES = {
    1: "Log a New Workout",
    2: "View Previous Workouts",
    3: "Log Meal",
    4: "View Food Logs",
    5: "Look up caloric value of excercise",
    6: "Look up caloric value of food",
    7: "Look up Supplement prices",
}


def display_choices(choices: dict):
    for choice, name in choices.items():
        print(f"{choice}. {name}")


def main():
    display_choices(CHOICES)
    choice = input("Select an option by entering its number:")

    try:
        choice = int(choice)
    except ValueError:
        print(f"Invalid input. Please enter a valid number.")
    if not (1 <= choice <= NUM_MENU_ITEMS):
        raise IndexError
    elif not (1 <= choice <= CURRENTLY_IMPLEMENTED):
        raise NotImplementedError


if __name__ == "__main__":
    main()
