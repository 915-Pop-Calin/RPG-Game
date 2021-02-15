from Abilities.SpaghettiMonsterAbilities.DefensiveStance import DefensiveStance
from Abilities.SpaghettiMonsterAbilities.Entangle import Entangle
from Characters.Character import Character
from Items.Armors.LevelOne.TemArmor import TemArmor
from Items.Weapons.LevelOne.Words import Words


class SpaghettiMonster(Character):
    def __init__(self):
        super().__init__("Spaghetti Monster", 1, 300, Words(), TemArmor(), 100, "Represents the developer")
        #super().__init__("Spaghetti Monster", 1, 300, Words(), TemArmor(), 10000, "Represents the developer")
        self.add_ability("entangle", self.entangle)
        self.add_ability("defensivestance", self.defensivestance)

    def entangle(self, opponent, list_of_turns, turn_counter):
        ability = Entangle()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string

    def defensivestance(self, opponent, list_of_turns, turn_counter):
        ability = DefensiveStance()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string