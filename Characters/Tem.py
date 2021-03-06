import random

from Abilities.TemAbilities.DoNothing import DoNothing
from Abilities.TemAbilities.HealTem import HealTem
from Characters.Character import Character
from Items.Armors.LevelOne.Cloth import Cloth
from Items.Weapons.LevelOne.Eclipse import Eclipse


class Tem(Character):
    def __init__(self):
        super().__init__("Tem", 1, 100, Eclipse(), Cloth(), 20, "Comes from Temmie Village\n")
        #super().__init__("Tem", 20, 100, Eclipse(), Cloth(), 20000, "Comes from Temmie Village.")
        self.add_ability("donothing", self.donothing)
        self.add_ability("healtem", self.healtem)

    def donothing(self, opponent, list_of_turns, turn_counter):
        ability = DoNothing()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string

    def healtem(self, opponent, list_of_turns, turn_counter):
        ability = HealTem()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string
