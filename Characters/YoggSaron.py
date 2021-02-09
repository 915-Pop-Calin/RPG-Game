import math

from Abilities.YoggSaronAbilities.Madness import Madness
from Characters.Character import Character
from Items.Armors.BootsOfDodge import BootsOfDodge
from Items.Weapons.BoilingBlood import BoilingBlood


class YoggSaron(Character):
    def __init__(self):
        super().__init__("Yogg Saron", math.inf, math.inf, BoilingBlood(), BootsOfDodge(), math.inf)
        self._discourage_counter = 3

    def set_attack_value(self, value):
        self._attack = value
        if self._discourage_counter > 0:
            print("Yogg Saron's touch on this world slips a bit!\n")
        self._discourage_counter -= 1
        if self._discourage_counter == 0:
            print("Yogg Saron's touch on this world fully slipped!\n")
            self.form_change()

    def form_change(self):
        print("Avatar of Yogg Saron appears!\n")
        self._name = "Avatar of Yogg Saron"
        self._innate_attack = 10
        self._innate_defense = 100
        self._health = 100
        self.re_set_attack_health()
        self._options = {"madness": self.madness}
        self._is_autoattacker = False

    def madness(self, opponent, list_of_turns, turn_counter):
        ability = Madness()
        string = ability.cast(self, opponent, list_of_turns, turn_counter)
        return string