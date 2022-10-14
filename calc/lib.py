from models import *

commoner = Creature("Commoner", 4.5, 10, {})
commoner.add_attack("Club", 2, 2.5)

armored_commoner = Creature("Armored Commoner", 4.5, 13, {})
armored_commoner.add_attack("Club", 2, 2.5)

orc = Creature("Orc", 15, 13, {})
orc.add_attack("Club", 5, 6.5)
orc.add_attack("Club", 5, 9.5)

tarrasque = Creature("Tarrasque", 676, 25, {})
tarrasque.add_attack("Bite", 19, 36)
tarrasque.add_attack("Claw", 19, 28)
tarrasque.add_attack("Horns", 19, 32)
tarrasque.add_attack("Tail", 19, 24)