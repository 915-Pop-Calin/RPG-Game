from Items.Weapons.Weapon import Weapon


class Words(Weapon):
    def __init__(self):
        super().__init__(0, 0)

    def get_id(self):
        return 204