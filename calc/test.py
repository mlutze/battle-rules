from calc import *
from models import *
from lib import *

P = 2
H = 100
S = 20
M = 1

units = [
    orc * 30,
    commoner * 30,
    tarrasque * 1
]

A = pickAByMaxHit(units, P = P, H = H, S = S, M = M)
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
# print("Orc: ")
# n_orc = n(30 * orc, params)
# for attack in orc.attacks:
#     t_orc = t(attack, params)
#     print(f"{n_orc}/{t_orc}")
# print("=" * 79)
# print("Commoner: ")
# n_comm = n(30 * commoner, params)
# for attack in commoner.attacks:
#     t_comm = t(attack, params)
#     print(f"{n_comm}/{t_comm}")
# print("Tarrasque: ")
# n_tarr = n(1 * tarrasque, params)
# for attack in tarrasque.attacks:
#     t_tarr = t(attack, params)
#     print(f"{n_tarr}/{t_tarr}")