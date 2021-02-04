from Items.Weapons.Weapon import Weapon

class Eclipse(Weapon):
    def __init__(self):
        super().__init__(5, -2)

    def get_id(self):
        return 201