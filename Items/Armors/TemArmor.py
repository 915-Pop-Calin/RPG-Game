from Items.Armors.Armour import Armour


class TemArmor(Armour):
    def __init__(self):
        super().__init__(0, 100)

    def get_id(self):
        return 302