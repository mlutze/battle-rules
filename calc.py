from math import ceil
from typing import NamedTuple

class Attack(NamedTuple):
    bonus: int
    damage: float

class Creature(NamedTuple):
    health: float
    ac: int
    attacks: list[Attack]

class Unit(NamedTuple):
    creature: Creature
    size: int

class Parameters(NamedTuple):
    P: float
    A: float
    H: float
    S: int

def n(unit: Unit, params: Parameters) -> int:
    num = unit.creature.health * unit.size * unit.creature.ac ** params.P
    denom = 10 ** params.P * params.H
    return ceil(num / denom)

def t(attack: Attack, creature: Creature, params: Parameters) -> int:
    num = attack.damage * (10 + attack.bonus) ** params.P * params.H * params.S
    denom = creature.health * creature.ac ** params.P * params.A
    return 20 - ceil(num / denom)

def ratio(attack: Attack, creature: Creature, P: float) -> float:
    num = attack.damage * (10 + attack.bonus) ** P
    denom = creature.health * creature.ac ** P
    return num / denom

commoner_club = Attack(2, 2.5)
commoner = Creature(4.5, 10, [commoner_club])
commoner_100 = Unit(commoner, 100)

armored_commoner = Creature(4.5, 13, [commoner_club])
armored_commoner_100 = Unit(armored_commoner, 100)

orc_javelin = Attack(5, 6.5)
orc_greataxe = Attack(5, 9.5)
orc = Creature(15, 13, [orc_javelin, orc_greataxe])
orc_20 = Unit(orc, 20)

print(n(commoner_100, Parameters(P = 2, A = 100, H = 100, S = 20)))
print(t(commoner_club, commoner, Parameters(P = 2, A = 100, H = 100, S = 20)))

print(n(armored_commoner_100, Parameters(P = 2, A = 100, H = 100, S = 20)))
print(t(commoner_club, armored_commoner, Parameters(P = 2, A = 100, H = 100, S = 20)))

print(n(orc_20, Parameters(P = 2, A = 100, H = 100, S = 20)))
print(t(orc_javelin, orc, Parameters(P = 2, A = 100, H = 100, S = 20)))
print(t(orc_greataxe, orc, Parameters(P = 2, A = 100, H = 100, S = 20)))
