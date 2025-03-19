from game import Game
import random
from character import Character
from charactertype import CharacterType

alice = Character(name="Alice", character_type=CharacterType.WARRIOR, health=100, attack_power=25)
bob = Character(name="Bob", character_type=CharacterType.MAGE, health=70, attack_power=15)

random_roll = random.randint(1,6)
print("Random roll: {random_roll}")

game = Game(alice, bob)
game.start_battle()

