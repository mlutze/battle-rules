from calc import *
from models import *
from lib import *
from sim import *

P = 2
S = 20
n_star = 10
x_star = n_star
t_star = 0

orcs = [orc * 50] * 20
dryads = [dryad * 50] * 4
knights = [knight * 25] * 4
rebels = [armored_commoner * 50] * 4
zealots = [armored_commoner * 50] * 8

units = [
    young_easthamite * 50,
    mounted_young_easthamite * 50,
    easthamite * 50,
    orc * 50,
    dryad * 50,
    knight.named("Royal Guard") * 25,
    giant_elk.named("Breachdweller") * 25,
]

H = pickHByMinHealth(units, P = P, n_star = n_star)
A1 = pickAByAvgDamage(units, P = P, H = H, x_star = x_star)
A2 = pickAByMinTarget(units, P = P, H = H, S = S, t_star = t_star)
A = max(A1, A2)
F = pickFByAvgSurfaceAreaRatio(units)
G1 = pickGByMinSize(units)
G2 = pickGByMinSpeed(units, A = A, H = H, F = F)
G = min(G1, G2)
print("H =", H)
print("A1 =", A1)
print("A2 =", A2)
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
        x_value = x(attack, G = G)
        print(f"{name}: {n_value}/{t_value} ({x_value})")
        print(f"- average damage: {expected_damage(n_value=n_value, t_value=t_value, S=S)}")
    print()

print(f"Time per round: {time_per_round} seconds")
print(f"Grid size: {G} feet")