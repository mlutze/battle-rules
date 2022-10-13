from typing import NamedTuple

class Attack(NamedTuple):
    bonus: int
    damage: float
    creature: "Creature"

class Creature(NamedTuple):
    health: float
    ac: int
    attacks: list[Attack]

    def add_attack(self, bonus: int, damage: float) -> Attack:
        attack = Attack(bonus, damage, self)
        self.attacks.append(attack)
        return attack

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