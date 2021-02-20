from Items.Weapons.Weapon import Weapon


class GiantSlayer(Weapon):
    def __init__(self):
        super().__init__(20, 0)
        self._armor_pen = 0.4
        self._description = "Great against high armour monsters.\n"

    def get_id(self):
        return 215