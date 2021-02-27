import random

from Items.Weapons.Weapon import Weapon


class TheRing(Weapon):
    def __init__(self):
        super().__init__(1, 0)
        self.set_effect()
        self._description = "Scaling weapon. Starts of very weak but gains one attack on each attack.\n"

    def effect(self, damage, caster, opponent):
        attack_value = self.attack_value()
        choice = random.randint(1, 4)
        string = ""
        if choice == 1:
            opponent.reduce_sanity(attack_value)
            sanity = opponent.get_sanity()
            string = opponent.get_name() + "'s sanity was reduced by " + str(attack_value) + "!\n"
            string += opponent.get_name() + " is left with " + str(sanity) + " sanity!\n"
        self.increment_attack_value()
        string += caster.get_name() + "'s weapon attack was increased by 1!\n"
        caster.re_set_attack_health()
        return string
