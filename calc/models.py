from dataclasses import dataclass, field
from typing import NamedTuple, Optional
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

@dataclass(frozen=True)
class Creature:
    name: str
    size: Size
    health: float
    ac: int
    attacks: dict[str, Attack] = field(default_factory=dict)

    def __mul__(self, size: int) -> "Unit":
        return Unit(self, size)

    def __rmul__(self, size: int) -> "Unit":
        return Unit(self, size)
    
    def with_attack(self, name: str, bonus: int, damage: float) -> "Creature":
        that = Creature(self.name, self.size, self.health, self.ac)
        for att_name, att0 in self.attacks.items():
            att = Attack(att0.name, att0.bonus, att0.damage, that)
            that.attacks[att_name] = att
        that.attacks[name] = Attack(name, bonus, damage, that)
        return that
    
class Unit(NamedTuple):
    creature: Creature
    size: int

class Parameters(NamedTuple):
    P: float
    A: float
    H: float
    S: int