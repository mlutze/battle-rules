from calc import *
from models import *
from lib import *
from sim import *

P = 2
S = 20
n_star = 10
t_star = 30
x_star = n_star / 4

units = [
    commoner * 100, 
    orc * 30,
    # tarrasque * 1
]

H = pickHByMinHealth(units, P = P, n_star = n_star)
# A = pickAByMinHurdle(units, P = P, H = H, S = S, t_star = t_star)
A = pickAByAvgDamage(units, P = P, H = H, x_star = x_star)

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


one_win = 0
for i in range(50):
    if sim_1v1(*units, params) == 1:
        one_win += 1
for i in range(50):
    if sim_1v1(*reversed(units), params) == 2:
        one_win += 1

print(f"{units[0].creature.name} won {one_win}% of battles.")