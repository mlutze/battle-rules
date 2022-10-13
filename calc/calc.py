from math import ceil
from itertools import chain
from models import *

def n(unit: Unit, params: Parameters) -> int:
    num = unit.creature.health * unit.size * unit.creature.ac ** params.P
    denom = 10 ** params.P * params.H
    return ceil(num / denom)

def t(attack: Attack, params: Parameters) -> int:
    num = attack.damage * (10 + attack.bonus) ** params.P * params.H * params.S
    denom = attack.creature.health * attack.creature.ac ** params.P * params.A
    return 20 - ceil(num / denom)

def ratio(attack: Attack, P: float) -> float:
    num = attack.damage * (10 + attack.bonus) ** P
    denom = attack.creature.health * attack.creature.ac ** P
    return num / denom

def pickAByMaxHit(units: list[Unit], P: float, H: float, S: float, M: int) -> float:
    attacks = chain.from_iterable(unit.creature.attacks for unit in units)
    max_attack: Attack = max(attacks, key=lambda a: ratio(a, P))
    num = max_attack.damage * (10 + max_attack.bonus) ** P * H * S
    denom = max_attack.creature.health * max_attack.creature.ac ** P * (S - M)
    return num / denom
