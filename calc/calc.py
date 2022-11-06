from itertools import chain
from math import sqrt
from models import *

def median(l: list, key):
    l = sorted(l, key = key)
    return l[len(l) // 2]

def n(unit: Unit, P: float, H: float) -> int:
    num = unit.creature.health * unit.size * unit.creature.ac ** P
    denom = 10 ** P * H
    return round(num / denom)

def t(attack: Attack, params: Parameters) -> int:
    num = attack.damage * (10 + attack.bonus) ** params.P * params.H * params.S
    denom = attack.creature.health * attack.creature.ac ** params.P * params.A
    return params.S - round(num / denom)

def expected_damage(n_value: int, t_value: int, params: Parameters) -> float:
    return n_value * (params.S - t_value) / params.S

def attack_ratio(attack: Attack, P: float) -> float:
    num = attack.damage * (10 + attack.bonus) ** P
    denom = attack.creature.health * attack.creature.ac ** P
    return num / denom

def pickAByMinHurdle(units: list[Unit], P: float, H: float, S: float, t_star: int) -> float:
    attacks = chain.from_iterable(unit.creature.attacks.values() for unit in units)
    max_attack: Attack = max(attacks, key=lambda a: attack_ratio(a, P))
    num = max_attack.damage * (10 + max_attack.bonus) ** P * H * S
    denom = max_attack.creature.health * max_attack.creature.ac ** P * (S - t_star)
    return num / denom

def pickAByMaxHurdle(units: list[Unit], P: float, H: float, S: float, t_star: int) -> float:
    attacks = chain.from_iterable(unit.creature.attacks.values() for unit in units)
    min_attack: Attack = min(attacks, key=lambda a: attack_ratio(a, P))
    num = min_attack.damage * (10 + min_attack.bonus) ** P * H * S
    denom = min_attack.creature.health * min_attack.creature.ac ** P * (S - t_star)
    return num / denom

# TODO maybe change to max attack of each unit
def pickAByAvgDamage(units: list[Unit], P: float, H: float, x_star: int) -> float:
    attacks = chain.from_iterable([(unit, attack) for attack in unit.creature.attacks.values()] for unit in units)
    avg_attack: Attack = median(attacks, key=lambda a: n(a[0], P = P, H = H) * attack_ratio(a[1], P))
    unit: Unit = avg_attack[0]
    attack: Attack = avg_attack[1]
    num =  n(unit, P = P, H = H) * attack.damage * (10 + attack.bonus) ** P * H
    denom = attack.creature.health * attack.creature.ac ** P * x_star
    return num / denom

def health_factor(unit: Unit, P: float) -> float:
    return unit.creature.health * unit.size * unit.creature.ac ** P

def pickHByMaxHealth(units: list[Unit], P: float, n_star: int) -> float:
    max_unit = max(units, key=lambda u: health_factor(u, P))
    num = max_unit.creature.health * max_unit.size * max_unit.creature.ac ** P
    denom = 10 ** P * n_star
    return num / denom

def pickHByMinHealth(units: list[Unit], P: float, n_star: int) -> float:
    min_unit = min(units, key=lambda u: health_factor(u, P))
    num = min_unit.creature.health * min_unit.size * min_unit.creature.ac ** P
    denom = 10 ** P * n_star
    return num / denom

def pickFByAvgSurfaceAreaRatio(units: list[Unit]) -> float:
    avg_unit = median(units, lambda u: u.size)
    num = avg_unit.size - (sqrt(avg_unit.size) - 2) ** 2
    denom = avg_unit.size
    return num / denom

def size_factor(unit: Unit) -> float:
    return sqrt(unit.size ** 2 * unit.creature.size.value)

def e(unit: Unit, G: float) -> float:
    num = sqrt(unit.size ** 2 * unit.creature.size.value)
    denom = G
    return round(num / denom)

def pickGByMinSize(units: list[Unit]) -> float:
    min_unit = min(units, key=size_factor)
    return sqrt(min_unit.size ** 2 * min_unit.creature.size.value)

def s(A: float, H: float, F: float) -> float:
    num = 3 * A
    denom = H * F
    return num / denom

def m(p: int, A: float, H: float, F: float, G: float) -> float:
    num = p * A
    denom = 12 * H * F * G
    return num / denom