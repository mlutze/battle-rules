from models import *

commoner = Creature("Commoner", Size.Medium, 4.5, 10) \
    .with_attack("Club", 2, 2.5) \

armored_commoner = Creature("Armored Commoner", Size.Medium, 4.5, 13) \
    .with_attack("Club", 2, 2.5) \

orc = Creature("Orc", Size.Medium, 15, 13) \
    .with_attack("Javelin", 5, 6.5) \
    .with_attack("Greataxe", 5, 9.5) \

tarrasque = Creature("Tarrasque", Size.Gargantuan, 676, 25) \
    .with_attack("Bite", 19, 36) \
    .with_attack("Claw", 19, 28) \
    .with_attack("Horns", 19, 32) \
    .with_attack("Tail", 19, 24) \

frog = Creature("Frog", Size.Tiny, 1.5, 11) \

knight = Creature("Knight", Size.Medium, 52, 19) \
    .with_attack("Greatsword", 5, 10) \
    .with_attack("Heavy Crossbow", 2, 5.5) \
    .with_attack("Multiattack", 5, 20) \

bandit = Creature("Bandit", Size.Medium, 11, 12) \
    .with_attack("Scimitar", 3, 4.5) \
    .with_attack("Light Crossbow", 3, 5.5) \

kobold = Creature("Kobold", Size.Small, 5, 12) \
    .with_attack("Dagger", 4, 4.5) \
    .with_attack("Sling", 4, 4.5) \

dryad = Creature("Dryad", Size.Medium, 22.5, 16) \
    .with_attack("Club With Shillelagh", 6, 8.5) \

harpy = Creature("Harpy", Size.Medium, 38.5, 11) \
    .with_attack("Claws", 3, 6) \
    .with_attack("Club", 3, 3.5) \
    .with_attack("Multiattack", 3, 9.5) \

bugbear = Creature("Bugbear", Size.Medium, 27.5, 16) \
    .with_attack("Morningstar", 4, 11) \
    .with_attack("Javelin", 4, 9) \

elephant = Creature("Elephant", Size.Huge, 76, 12) \
    .with_attack("Gore", 8, 19.5) \
    .with_attack("Stomp", 8, 19.5) \
    .with_attack("Trampling Charge", 8, 39) \

pass