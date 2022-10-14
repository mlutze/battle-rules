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

frog = Creature("Frog", 1.5, 11, {})

knight = Creature("Knight", 52, 18, {})
knight.add_attack("Greatsword", 5, 10)
knight.add_attack("Heavy Crossbow", 2, 5.5)

bandit = Creature("Bandit", 11, 12)
bandit.add_attack("Scimitar", 3, 4.5)
bandit.add_attack("Light Crossbow", 3, 5.5)