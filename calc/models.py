from typing import NamedTuple
from enum import Enum

class Size(Enum):
    Tiny = 2.5
    Small = 5
    Medium = 5
    Large = 10
    Huge = 15
    Gargantuan = 20

class Attack(NamedTuple):
    name: str
    bonus: int
    damage: float
    creature: "Creature"

class Creature(NamedTuple):
    name: str
    size: Size
    health: float
    ac: int
    attacks: dict[str, Attack]

    def add_attack(self, name: str, bonus: int, damage: float) -> Attack:
        attack = Attack(name, bonus, damage, self)
        self.attacks[name] = attack

    def __mul__(self, size: int) -> "Unit":
        return Unit(self, size)

    def __rmul__(self, size: int) -> "Unit":
        return Unit(self, size)
    
class Unit(NamedTuple):
    creature: Creature
    size: int

class Parameters(NamedTuple):
    P: float
    A: float
    H: float
    S: int