from enum import Enum
from charactertype import CharacterType

class CharacterType(Enum):
    WARRIOR= "Warrior"
    MAGE= "Mage"
    ROGUE= "Rogue"

my_charactertype_type = CharacterType.MAGE

