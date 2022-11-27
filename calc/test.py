from calc import *
from models import *
from lib import *
from sim import *

P = 2
S = 20
n_star = 10
x_star = n_star / 4

units = [
    kobold * 30,
    harpy * 10,
    giant_badger * 40,
    giant_badger * 40,
    cultist * 100,
    elephant * 8,
    tarrasque * 1,
    diseased_rat * 30,
]

H = pickHByMinHealth(units, P = P, n_star = n_star)
A = pickAByAvgDamage(units, P = P, H = H, x_star = x_star)
F = pickFByAvgSurfaceAreaRatio(units)
G1 = pickGByMinSize(units)
G2 = pickGByMinSpeed(units, A = A, H = H, F = F)
G = min(G1, G2)
print("H =", H)
print("A =", A)
print("F =", F)
print("P =", P)
print("S =", S)
print("G1 =", G1)
print("G2 =", G2)
print("G =", G)

print()
time_per_round = s(A, H, F)
for unit in units:
    print(f"=== {unit.creature.name} ({unit.size}) ===")
    n_value = n(unit, H = H, P = P)
    edge = e(unit, G)
    speed = m(unit, A, H, F, G)
    print(f"Speed: {speed}")
    print(f"Size: {edge}x{edge}")
    print(f"Dice: {n_value}")
    for name, attack in unit.creature.attacks.items():
        t_value = t(attack, P = P, H = H, S = S, A = A)
        print(f"{name}: {n_value}/{t_value}")
    print()

print(f"Time per round: {time_per_round} seconds")