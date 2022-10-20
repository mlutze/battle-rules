from calc import *
from models import *
from lib import *
from sim import *

P = 2
S = 20
T = 0.5
n_star = 10
t_star = 30
x_star = n_star / 4

units = [
    kobold * 30, 
    bandit * 7,
    bandit * 7,
    bandit * 7,
    dryad * 15,
    armored_commoner * 20,
    orc * 20,
    commoner * 20
]

H = pickHByMinHealth(units, P = P, n_star = n_star)
A = pickAByAvgDamage(units, P = P, H = H, x_star = x_star)
F = pickFByAvgSurfaceAreaRatio(units)
print("F =", F)

params = Parameters(P = P, A = A, H = H, S = S)
print(params)
print()
for unit in units:
    print(f"=== {unit.creature.name} ({unit.size}) ===")
    n_value = n(unit, H = H, P = P)
    print(f"Dice: {n_value}")
    for name, attack in unit.creature.attacks.items():
        t_value = t(attack, params)
        print(f"{name}: {n_value}/{t_value}")
    print()

print(f"Time per round: {A / H / F / T * 6} seconds")