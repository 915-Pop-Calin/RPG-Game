import random

from Items.Weapons.Weapon import Weapon


class Dreams(Weapon):
    def __init__(self):
        super().__init__(2, 0)
        self.set_effect()
        self._description = "Makes your enemy go insane. Has no effect on most monsters\n"

    def effect(self, damage, caster, opponent):
        choice = random.randint(1,1)
        string = ""
        if choice == 1:
            madness_inducer = random.randint(15, 25)
            opponent.reduce_sanity(madness_inducer)
            string = opponent.get_name() + "\b's sanity was reduced by " + str(madness_inducer) + "!\n"
            string += opponent.get_name() + " has " + str(opponent.get_sanity()) + " sanity left!\n"
        return string
