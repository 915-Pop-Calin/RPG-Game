from Items.Armors.Armour import Armour


class Cloth(Armour):
    def __init__(self):
        super().__init__(0, 2)

    def get_id(self):
        return 301