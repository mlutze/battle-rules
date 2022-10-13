from models import *

commoner = Creature(4.5, 10, [])
commoner_club = commoner.add_attack(2, 2.5)

armored_commoner = Creature(4.5, 13, [])
armored_commoner_club = armored_commoner.add_attack(2, 2.5)

orc = Creature(15, 13, [])
orc_javelin = orc.add_attack(5, 6.5)
orc_greataxe = orc.add_attack(5, 9.5)

tarrasque = Creature(676, 25, [])
tarrasque_bite = tarrasque.add_attack(19, 36)
tarrasque_claw = tarrasque.add_attack(19, 28)
tarrasque_horns = tarrasque.add_attack(19, 32)
tarrasque_tail = tarrasque.add_attack(19, 24)