from models import *

commoner = Creature("Commoner", Size.Medium, 4.5, 10, 30) \
    .with_melee_attack("Club", 2, 2.5, 5) \

armored_commoner = Creature("Armored Commoner", Size.Medium, 4.5, 13, 30) \
    .with_melee_attack("Club", 2, 2.5, 5) \

tarrasque = Creature("Tarrasque", Size.Gargantuan, 676, 25, 40) \
    .with_melee_attack("Bite", 19, 36, 10) \
    .with_melee_attack("Claw", 19, 28, 15) \
    .with_melee_attack("Horns", 19, 32, 10) \
    .with_melee_attack("Tail", 19, 24, 20) \
    .with_multiattack("Multiattack", ["Bite", "Claw", "Claw", "Horns", "Tail"]) \

frog = Creature("Frog", Size.Tiny, 1.5, 11, 20) \

giant_frog = Creature("Giant Frog", Size.Medium, 18, 11, 30) \
    .with_melee_attack("Bite", 3, 3.5, 5) \

knight = Creature("Knight", Size.Medium, 52, 19, 30) \
    .with_melee_attack("Greatsword", 5, 10, 5) \
    .with_ranged_attack("Heavy Crossbow", 2, 5.5, 100, 400) \
    .with_multiattack("Multiattack", ["Greatsword", "Greatsword"]) \

bandit = Creature("Bandit", Size.Medium, 11, 12, 30) \
    .with_melee_attack("Scimitar", 3, 4.5, 5) \
    .with_ranged_attack("Light Crossbow", 3, 5.5, 80, 320) \

kobold = Creature("Kobold", Size.Small, 5, 12, 30) \
    .with_melee_attack("Dagger", 4, 4.5, 5) \
    .with_ranged_attack("Sling", 4, 4.5, 30, 120) \

harpy = Creature("Harpy", Size.Medium, 38.5, 11, 40) \
    .with_melee_attack("Claws", 3, 6, 5) \
    .with_melee_attack("Club", 3, 3.5, 5) \
    .with_multiattack("Multiattack", ["Claws", "Club"]) \

bugbear = Creature("Bugbear", Size.Medium, 27.5, 16, 30) \
    .with_melee_attack("Morningstar", 4, 11, 5) \
    .with_melee_attack("Javelin", 4, 9, 5) \
    .with_ranged_attack("Javelin", 4, 9, 30, 120) \

elephant = Creature("Elephant", Size.Huge, 76, 12, 40) \
    .with_melee_attack("Gore", 8, 19.5, 5) \
    .with_melee_attack("Stomp", 8, 19.5, 5) \
    .with_multiattack("Trampling Charge", ["Gore", "Stomp"]) \

cultist = Creature("Cultist", Size.Medium, 9, 12, 30) \
    .with_melee_attack("Scimitar", 3, 4.5, 5) \

duergar = Creature("Duergar", Size.Medium, 26, 16, 25) \
    .with_melee_attack("War Pick", 4, 6.5, 5) \
    .with_melee_attack("Javelin (melee)", 4, 5.5, 5) \
    .with_ranged_attack("Javelin (ranged)", 4, 5.5, 30, 120) \

enlarged_duergar = Creature("Enlarged Duergar", Size.Large, 26, 16, 25) \
    .with_melee_attack("War Pick", 4, 11, 5) \
    .with_melee_attack("Javelin (melee)", 4, 9, 5) \
    .with_ranged_attack("Javelin (ranged)", 4, 9, 30, 120) \

diseased_giant_rat = Creature("Diseased Giant Rat", Size.Small, 7, 12, 30) \
    .with_melee_attack("Bite", 4, 4.5, 5) \

giant_badger = Creature("Giant Badger", Size.Medium, 13, 10, 30) \
    .with_melee_attack("Bite", 3, 4.5, 5) \
    .with_melee_attack("Claws", 3, 6, 5) \
    .with_multiattack("Multiattack", ["Bite", "Claws"]) \

ballista = Creature("Ballista", Size.Large, 50, 15, 15) \
    .with_ranged_attack("Bolt", 6, 16 / 3, 120, 480) \

trebuchet = Creature("Trebuchet", Size.Huge, 150, 15, 15) \
    .with_ranged_attack("Trebuchet Stone", 5, 44 / 5, 300, 1200) \
    
mangonel = Creature("Mangonel", Size.Large, 100, 15, 15) \
    .with_ranged_attack("Mangonel Stone", 5, 27 / 5, 200, 800) \

### BATTLE FOR THORPWARK ###
# AC: halfway betwen 12 (mastiff) and 13 (chain shirt)
mounted_young_easthamite = Creature("Mounted Young Easthamite", Size.Medium, 10, 12.5, 40) \
    .with_ranged_attack("Crossbow", 2, 4.5, 80, 320) \
    .with_melee_attack("Bite", 3, 4.5, 5)

# AC: 13 (chain shirt)
young_easthamite = Creature("Young Easthamite", Size.Small, 4.5, 13, 25) \
    .with_ranged_attack("Crossbow", 2, 4.5, 80, 320)

# AC: 13 (chain shirt) + 2 (shield)
easthamite = Creature("Easthamite", Size.Medium, 4.5, 15, 30) \
    .with_melee_attack("Spear", 2, 3.5, 5)

dryad = Creature("Dryad", Size.Medium, 22.5, 16, 30) \
    .with_melee_attack("Club With Shillelagh", 6, 8.5, 5) \

orc = Creature("Orc", Size.Medium, 15, 13, 30) \
    .with_melee_attack("Javelin (melee)", 5, 6.5, 5) \
    .with_melee_attack("Greataxe", 5, 9.5, 5) \
    .with_ranged_attack("Javelin (ranged)", 5, 6.5, 30, 120) \

giant_elk = Creature("Giant Elk", Size.Huge, 42, 14, 60) \
    .with_melee_attack("Ram", 6, 11, 10) \
    .with_melee_attack("Hooves", 6, 22, 5) \
    .with_melee_attack("Ramming Charge", 6, 18, 10) \

pass