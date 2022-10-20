from models import *

commoner = Creature("Commoner", Size.Medium, 4.5, 10, {})
commoner.add_attack("Club", 2, 2.5)

armored_commoner = Creature("Armored Commoner", Size.Medium, 4.5, 13, {})
armored_commoner.add_attack("Club", 2, 2.5)

orc = Creature("Orc", Size.Medium, 15, 13, {})
orc.add_attack("Javelin", 5, 6.5)
orc.add_attack("Greataxe", 5, 9.5)

tarrasque = Creature("Tarrasque", Size.Gargantuan, 676, 25, {})
tarrasque.add_attack("Bite", 19, 36)
tarrasque.add_attack("Claw", 19, 28)
tarrasque.add_attack("Horns", 19, 32)
tarrasque.add_attack("Tail", 19, 24)

frog = Creature("Frog", Size.Tiny, 1.5, 11, {})

knight = Creature("Knight", Size.Medium, 52, 19, {})
knight.add_attack("Greatsword", 5, 10)
knight.add_attack("Heavy Crossbow", 2, 5.5)
knight.add_attack("Multiattack", 5, 20)

bandit = Creature("Bandit", Size.Medium, 11, 12, {})
bandit.add_attack("Scimitar", 3, 4.5)
bandit.add_attack("Light Crossbow", 3, 5.5)

kobold = Creature("Kobold", Size.Small, 5, 12, {})
kobold.add_attack("Dagger", 4, 4.5)
kobold.add_attack("Sling", 4, 4.5)

dryad = Creature("Dryad", Size.Medium, 22.5, 16, {})
dryad.add_attack("Club With Shillelagh", 6, 8.5)

harpy = Creature("Harpy", Size.Medium, 38.5, 11, {})
harpy.add_attack("Claws", 3, 6)
harpy.add_attack("Club", 3, 3.5)
harpy.add_attack("Multiattack", 3, 9.5)

bugbear = Creature("Bugbear", Size.Medium, 27.5, 16, {})
bugbear.add_attack("Morningstar", 4, 11)
bugbear.add_attack("Javelin", 4, 9)

elephant = Creature("Elephant", Size.Huge, 76, 12, {})
elephant.add_attack("Gore", 8, 19.5)
elephant.add_attack("Stomp", 8, 19.5)
elephant.add_attack("Trampling Charge", 8, 39)