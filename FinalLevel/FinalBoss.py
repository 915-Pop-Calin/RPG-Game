import math
import random

from Characters.Character import Character
from FinalLevel.SaroniteScales import SaroniteScales
from FinalLevel.SaroniteTentacles import SaroniteTentacles


class FinalBoss(Character):
    def __init__(self):
        super().__init__("??????", 75, 10000, SaroniteTentacles(), SaroniteScales(), 10000, "Mysterious presence")
        self._phase = 1
        self._attack_type = "sanity"
        self._options = {"physical": self.physical, "sanity": self.insanity , "both": self.both}
        self._dialogue = ["I am the lucid dream", "The monster in your nightmares", "The fiend of a thousand faces",
                          "Bow down before me!"]

    def check_if_form_change(self):
        if self._phase == 1 and self._weapon.is_broken():
            self._phase = 2
            return True, 2
        elif self._phase == 2 and self._armor.is_broken():
            self._phase = 3
            return True, 3
        return False, 0

    def set_attack_type(self, type):
        self._attack_type = type

    def set_ultimate_form(self):
        self.set_innate_defense(10000000)

    def insanity(self, opponent):
        random_int = random.randint(1, 30)
        opponent.reduce_sanity(random_int)
        string = opponent.get_name() + "'s sanity was reduced by " + str(random_int) + "!\n"
        string += opponent.get_name() + " is left with " + str(opponent.get_sanity()) + " sanity!\n"
        string += self._dialogue[0]
        if len(self._dialogue) == 1:
            self._dialogue[0] = "..."
        else:
            self._dialogue.pop(0)
        return string

    def physical(self, opponent):
        string = self.hit(opponent, None, None)
        return string

    def both(self, opponent):
        string = self.insanity(opponent)
        string += self.physical(opponent)
        return string

    def get_options(self):
        return self._options

    def attack_type(self):
        return self._attack_type
