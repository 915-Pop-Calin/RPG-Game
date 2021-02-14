import random

from Abilities.TemAbilities.DoNothing import DoNothing
from Abilities.TemAbilities.HealTem import HealTem
from Characters.Character import Character
from Items.Armors.Cloth import Cloth
from Items.Armors.SaroniteScales import SaroniteScales
from Items.Weapons.Eclipse import Eclipse
from Items.Weapons.SaroniteTentacles import SaroniteTentacles


class Tem(Character):
    def __init__(self):
        super().__init__("Tem", 1, 100, Eclipse(), Cloth(), 20, "Comes from Temmie Village.")
        #super().__init__("Tem", -20, 100, SaroniteTentacles(), SaroniteScales(), 20, "Comes from Temmie Village.")
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
