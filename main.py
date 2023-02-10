import datetime
from collections import namedtuple
from excercise_objects import Set, Exercise, Workout, Meal, Ingredient

CURRENTLY_IMPLEMENTED = 1  # "Debug" value for me to change as I implement more features
APP_OPTION = namedtuple("APP_OPTION", ["label", "function"])


def init_db():
    pass


def log_workout(workout: Workout):
    pass


def log_meal(meal: Meal):
    pass


def create_set(set_num: int) -> Set:
    set_weight = input("Weight: ")
    set_num_reps = input("Number of reps: ")
    set = Set(set_num, set_weight, set_num_reps)
    return set


def create_exercise() -> Exercise:
    exc_name = input("Exercise name: ")
    exc = Exercise(exc_name)
    set_num = 1
    while True:
        set = create_set(set_num)
        exc.add_set(set)
        ans = input("Another set? (y/n): ")
        if ans == "y":
            set_num += 1
        else:
            break
    return exc


def create_workout() -> Workout:
    workout_name = input("Workout name: ")
    date = datetime.date.today()
    workout = Workout(date, workout_name)
    while True:
        exc = create_exercise()
        workout.add_exercise(exc)
        ans = input("Another exercise? (y/n): ")
        if ans == "n":
            break
    return workout


def view_workouts():
    pass


def create_ingredient() -> Ingredient:
    ingr_name = input("Ingredient name: ")
    ingr_weight = input("Ingredient weight: ")
    ingr_weight = float(ingr_weight)
    ingr = Ingredient(ingr_name, ingr_weight)
    return ingr


def create_meal() -> Meal:
    meal_name = input("Meal name: ")
    meal = Meal(meal_name)
    while True:
        ingr = create_ingredient()
        meal.add_ingredient(ingr)
        ans = input("Another ingredient? (y/n): ")
        if ans == "n":
            break
    return Meal


def view_meals():
    pass


def search_exercise():
    pass


def search_food():
    pass


def search_supplement():
    pass


OPTIONS = {
    1: APP_OPTION("Log a New Workout", create_workout),
    2: APP_OPTION("View Previous Workouts", view_workouts),
    3: APP_OPTION("Log Meal", create_meal),
    4: APP_OPTION("View Food Logs", view_meals),
    5: APP_OPTION("Look up caloric value of excercise", search_exercise),
    6: APP_OPTION("Look up caloric value of food", search_food),
    7: APP_OPTION("Look up supplement prices", search_supplement),
}
NUM_APP_OPTIONS = len(OPTIONS)


def display_options(options: dict):
    for number, option in options.items():
        print(f"{number}. {option.label}")


def main():
    display_options(OPTIONS)
    option = input("Select an option by entering its number:")

    try:
        option = int(option)
        OPTIONS.get(option).function()

    except ValueError:
        print(f"Invalid input. Please enter a valid number.")
    if not (1 <= option <= NUM_APP_OPTIONS):
        raise IndexError
    elif not (1 <= option <= CURRENTLY_IMPLEMENTED):
        raise NotImplementedError


if __name__ == "__main__":
    main()
