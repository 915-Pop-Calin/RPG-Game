from Items.Weapons.Weapon import Weapon


class Words(Weapon):
    def __init__(self):
        super().__init__(0, 0)
        self._description = "Words can't hurt you.\n"
