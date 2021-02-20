from Items.Weapons.Weapon import Weapon


class RadusBiceps(Weapon):
    def __init__(self):
        super().__init__(50, 0)
        self._crit_chance = -0.15
        self._description = "Huge attack, but it can not crit.\n"

    def get_id(self):
        return 213