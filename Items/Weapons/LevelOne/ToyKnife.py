from Items.Weapons.Weapon import Weapon


class ToyKnife(Weapon):
    def __init__(self):
        super().__init__(3, 0)
        self._description = "Is this a game?\n"
