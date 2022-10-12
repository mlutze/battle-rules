from math import ceil
from typing import NamedTuple
from itertools import chain

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

commoner = Creature(4.5, 10, [])
commoner_club = commoner.add_attack(2, 2.5)
commoner_100 = Unit(commoner, 100)
commoner_30 = Unit(commoner, 30)

armored_commoner = Creature(4.5, 13, [])
armored_commoner_club = armored_commoner.add_attack(2, 2.5)
armored_commoner_100 = Unit(armored_commoner, 100)

orc = Creature(15, 13, [])
orc_javelin = orc.add_attack(5, 6.5)
orc_greataxe = orc.add_attack(5, 9.5)
orc_mallet = orc.add_attack(10, 30)
orc_20 = Unit(orc, 20)
orc_6 = Unit(orc, 6)
orc_30 = Unit(orc, 30)

P = 2
H = 30
S = 20
M = 1

A = pickAByMaxHit([orc_30, commoner_30], P = P, H = H, S = S, M = M)
params = Parameters(P = P, A = A, H = H, S = S)
print(params)
print("=" * 79)
print("Orc: ")
n_orc = n(orc_30, params)
for attack in orc.attacks:
    t_orc = t(attack, params)
    print(f"{n_orc}/{t_orc}")
print("=" * 79)
print("Commoner: ")
n_comm = n(commoner_30, params)
for attack in commoner.attacks:
    t_comm = t(attack, params)
    print(f"{n_comm}/{t_comm}")

