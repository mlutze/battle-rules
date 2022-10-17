from calc import *
from lib import *
from random import randint

def sim_1v1(unit1: Unit, unit2: Unit, params: Parameters) -> None:
    n1 = n(unit1, params)
    n2 = n(unit2, params)
    t1 = min(t(attack, params) for _, attack in unit1.creature.attacks.items())
    t2 = min(t(attack, params) for _, attack in unit2.creature.attacks.items())

    while True:
        n2 -= roll(n1, t1)
        if n2 <= 0:
            return 1
        n1 -= roll(n2, t2)
        if n1 <= 0:
            return 2

def roll(n: int, h: int) -> int:
    hits = 0
    for _ in range(n):
        if randint(1, 20) > h:
            hits += 1
    return hits
