from dataclasses import dataclass, field
import datetime


@dataclass
class Set:
    set_num: int
    weight_kgs: float
    num_reps: int


@dataclass
class Exercise:
    name: str
    sets: list[Set] = field(default_factory=list)

    def add_set(self, set: Set):
        self.sets.append(set)


@dataclass
class Workout:
    date: datetime.datetime
    name: str
    exercises: list[Exercise] = field(default_factory=list)

    def add_exercise(self, exercise: Exercise):
        self.exercises.append(exercise)


@dataclass
class Ingredient:
    name: str
    weight_gs: float


@dataclass
class Meal:
    name: str
    ingredients: list[Ingredient] = field(default_factory=list)

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
