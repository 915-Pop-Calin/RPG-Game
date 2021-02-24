from Items.Weapons.Weapon import Weapon


class NoWeapon(Weapon):
    def __init__(self):
        super().__init__(0, 0)
        self._description = "You are wearing no weapon.\n"

    def get_id(self):
        return 217