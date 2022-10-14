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

def attack_ratio(attack: Attack, P: float) -> float:
    num = attack.damage * (10 + attack.bonus) ** P
    denom = attack.creature.health * attack.creature.ac ** P
    return num / denom

def pickAByMaxHit(units: list[Unit], P: float, H: float, S: float, t: int) -> float:
    attacks = chain.from_iterable(unit.creature.attacks.values() for unit in units)
    max_attack: Attack = max(attacks, key=lambda a: attack_ratio(a, P))
    num = max_attack.damage * (10 + max_attack.bonus) ** P * H * S
    denom = max_attack.creature.health * max_attack.creature.ac ** P * (S - t)
    return num / denom

def pickAByMinHit(units: list[Unit], P: float, H: float, S: float, t: int) -> float:
    attacks = chain.from_iterable(unit.creature.attacks.values() for unit in units)
    min_attack: Attack = min(attacks, key=lambda a: attack_ratio(a, P))
    num = min_attack.damage * (10 + min_attack.bonus) ** P * H * S
    denom = min_attack.creature.health * min_attack.creature.ac ** P * (S - t)
    return num / denom

def health_factor(unit: Unit, P: float) -> float:
    return unit.creature.health * unit.size * unit.creature.ac ** P

def pickHByMaxHealth(units: list[Unit], P: float, n: int) -> float:
    max_unit = max(units, key=lambda u: health_factor(u, P))
    num = max_unit.creature.health * max_unit.size * max_unit.creature.ac ** P
    denom = 10 ** P * n
    return num / denom

def pickHByMinHealth(units: list[Unit], P: float, n: int) -> float:
    min_unit = min(units, key=lambda u: health_factor(u, P))
    num = min_unit.creature.health * min_unit.size * min_unit.creature.ac ** P
    denom = 10 ** P * n
    return num / denom