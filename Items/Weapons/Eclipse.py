from Items.Weapons.Weapon import Weapon

class Eclipse(Weapon):
    def __init__(self):
        super().__init__(5, -2)
        self.set_life_steal(0.15)


    def get_id(self):
        return 201