from calc import *
from models import *
from lib import *

P = 2
H = 100
S = 20
n_star = 4
t_star = 1

units = [
    orc * 30,
    commoner * 30,
    tarrasque * 1
]

H = pickHByMinHealth(units, P = P, n_star = n_star)
A = pickAByMaxHit(units, P = P, H = H, S = S, t_star = t_star)

params = Parameters(P = P, A = A, H = H, S = S)
print(params)
print()
for unit in units:
    print(f"=== {unit.creature.name} ({unit.size}) ===")
    n_value = n(unit, params)
    print(f"Dice: {n_value}")
    for name, attack in unit.creature.attacks.items():
        t_value = t(attack, params)
        print(f"{name}: {n_value}/{t_value}")
    print()
