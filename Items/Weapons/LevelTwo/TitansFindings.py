import random

from Items.Weapons.Weapon import Weapon


class TitansFindings(Weapon):
    def __init__(self):
        super().__init__(5, 0)
        self.set_effect()
        self._description = "You restore sanity whenever you attack.\n"

    def effect(self, damage, caster, opponent):
        random_int = random.randint(1, 10)
        caster.restore_sanity(random_int)
        string = caster.get_name() + " has restored " + str(random_int) + " of his sanity!\n"
        string += caster.get_name() + " is left with " + str(caster.get_sanity()) + " sanity!\n"
        return string

    def get_id(self):
        return 211