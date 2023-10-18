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
    bonus: float
    damage: float
    short: float
    long: float
    creature: "Creature"

@dataclass(frozen=True)
class Creature:
    name: str
    size: Size
    health: float
    ac: int
    speed: int
    attacks: dict[str, Attack] = field(default_factory=dict)

    def __mul__(self, size: int) -> "Unit":
        return Unit(self, size)

    def __rmul__(self, size: int) -> "Unit":
        return Unit(self, size)

    def with_attack(self, name: str, bonus: float, damage: float, short: int, long: int) -> "Creature":
        that = Creature(self.name, self.size, self.health, self.ac, self.speed)
        for att_name, att0 in self.attacks.items():
            att = Attack(att0.name, att0.bonus, att0.damage, att0.short, att0.long, that)
            that.attacks[att_name] = att
        that.attacks[name] = Attack(name, bonus, damage, short, long, that)
        return that
    
    def with_melee_attack(self, name: str, bonus: float, damage: float, reach: int) -> "Creature":
        short = reach
        long = reach
        return self.with_attack(name, bonus, damage, short, long)
    
    def with_multiattack(self, name: str, att_names: list[str]) -> "Creature":
        atts = [self.attacks[att_name] for att_name in att_names]
        bonus = sum(att.bonus for att in atts) / len(atts)
        damage = sum(att.damage for att in atts)
        short = min(att.short for att in atts)
        long = min(att.long for att in atts)
        return self.with_attack(name, bonus, damage, short, long)
    
    def with_ranged_attack(self, name: str, bonus: float, damage: float, short: int, long: int) -> "Creature":
        return self.with_attack(name, bonus, damage, short, long)
    
    def named(self, name: str) -> "Creature":
        return Creature(name, self.size, self.health, self.ac, self.speed, self.attacks)
    
class Unit(NamedTuple):
    creature: Creature
    size: int

class Parameters(NamedTuple):
    P: float
    A: float
    H: float
    S: int