from calc import *
from models import *
from lib import *

P = 2
H = 100
S = 20
M = 1


A = pickAByMaxHit([30 * orc, 30 * commoner, 1 * tarrasque], P = P, H = H, S = S, M = M)
params = Parameters(P = P, A = A, H = H, S = S)
print(params)
print("=" * 79)
print("Orc: ")
n_orc = n(30 * orc, params)
for attack in orc.attacks:
    t_orc = t(attack, params)
    print(f"{n_orc}/{t_orc}")
print("=" * 79)
print("Commoner: ")
n_comm = n(30 * commoner, params)
for attack in commoner.attacks:
    t_comm = t(attack, params)
    print(f"{n_comm}/{t_comm}")
print("Tarrasque: ")
n_tarr = n(1 * tarrasque, params)
for attack in tarrasque.attacks:
    t_tarr = t(attack, params)
    print(f"{n_tarr}/{t_tarr}")