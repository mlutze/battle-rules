from lib import *
from calc import *

def print_stats(unit: Unit, *, P: float, H: float, S: int, A: float) -> None:
    n_value = n(unit, P = P, H = H)
    print(f"n = {n_value}")
    for name, attack in unit.creature.attacks.items():
        abbr = name[0].lower()
        t_value = t(attack, P = P, H = H, S = S, A = A)
        print(f"t_{abbr} = {t_value}")
        dmg = expected_damage(n_value = n_value, t_value = t_value, S = S)
        print(f"dmg_{abbr} = {dmg}")

print("=" * 80)

print("Unit of 20 Orcs")
P = 2
A = 100
H = 100
S = 20
print_stats(orc * 20, P = P, H = H, A = A, S = S)

print("=" * 80)

print("Armored vs Unarmored Commoners")
P = 2
A = 100
H = 100
S = 20
print("Commoner")
print_stats(commoner * 100, P = P, H = H, A = A, S = S)
print("Armored Commoner")
print_stats(armored_commoner * 100, P = P, H = H, A = A, S = S)

print("=" * 80)