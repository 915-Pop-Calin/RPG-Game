from Abilities.SpaghettiMonsterAbilities.DefensiveStance import DefensiveStance
from Abilities.SpaghettiMonsterAbilities.Entangle import Entangle
from Characters.Character import Character
from Items.Armors.TemArmor import TemArmor
from Items.Weapons.Words import Words


class SpaghettiMonster(Character):
    def __init__(self):
        super().__init__("Spaghetti Monster", 1, 0, Words(), TemArmor(), 30, "Represents the developer")
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