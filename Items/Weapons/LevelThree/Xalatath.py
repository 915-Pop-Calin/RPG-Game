import random
from Items.Weapons.Weapon import Weapon


class Xalatath(Weapon):
    def __init__(self):
        super().__init__(15, 0)
        self.set_life_steal(0.75)
        self._description = "VERY strong lifestealer which helps you not go insane.\n"
        self.set_effect()

    def effect(self, damage, caster, opponent):
        minimum_val = (damage // 2).__floor__()
        maximum_val = damage.__floor__()
        random_int = random.randint(minimum_val, maximum_val)
        caster.restore_sanity(random_int)
        string = caster.get_name() + " has restored " + str(random_int) + " of his sanity!\n"
        string += caster.get_name() + " is left with " + str(caster.get_sanity()) + " sanity!\n"
        return string

    def get_id(self):
        return 212
