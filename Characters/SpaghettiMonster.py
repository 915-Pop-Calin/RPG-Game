from Characters.Character import Character
from Items.Armors.TemArmor import TemArmor
from Items.Weapons.Words import Words


class SpaghettiMonster(Character):
    def __init__(self):
        super().__init__("Spaghetti Monster", 1, 0, Words(), TemArmor(), 30, "Represents the developer")
        self.options = [self.hit]
