from dataclasses import dataclass, field
import datetime


@dataclass
class Set:
    number: int
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
    date: datetime.date
    name: str
    exercises: list[Exercise] = field(default_factory=list)

    def add_exercise(self, exercise: Exercise):
        self.exercises.append(exercise)
