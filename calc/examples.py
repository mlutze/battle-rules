from lib import *
from calc import *

def print_stats(unit: Unit, params: Parameters) -> None:
    n_value = n(unit, params)
    print(f"n = {n_value}")
    for name, attack in unit.creature.attacks.items():
        abbr = name[0].lower()
        t_value = t(attack, params)
        print(f"t_{abbr} = {t_value}")
        dmg = expected_damage(n_value, t_value, params)
        print(f"dmg_{abbr} = {dmg}")

print("=" * 80)

print("Unit of 20 Orcs")
params = Parameters(P = 2, A = 100, H = 100, S = 20)
print_stats(orc * 20, params)

print("=" * 80)

print("Armored vs Unarmored Commoners")
params = Parameters(P = 2, A = 100, H = 100, S = 20)
print("Commoner")
print_stats(commoner * 100, params)
print("Armored Commoner")
print_stats(armored_commoner * 100, params)

print("=" * 80)

print("Strongest Must Roll 2")
P = 2
print("Commoner Ratio:", attack_ratio(commoner.attacks["Club"], P))
print("Orc Ratio:", attack_ratio(orc.attacks["Greataxe"], P))
H = 100
S = 20
A = pickAByMinHurdle([commoner * 100, orc * 20], P = P, H = 100, S = 20, t_star = 2)
print("A:", A)
params = Parameters(P = P, A = A, H = H, S = S)
print("Orc")
print_stats(orc * 20, params)
print("Commoner")
print_stats(commoner * 100, params)
