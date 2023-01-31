from dataclasses import dataclass


@dataclass
class Set:
    weight_kgs: float
    num_reps: int


@dataclass
class Exercise:
    name: str
    sets: list[Set]


@dataclass
class Workout:
    date: str
    name: str
    exercises: list[Exercise]
