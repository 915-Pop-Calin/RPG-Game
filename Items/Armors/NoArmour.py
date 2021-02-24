from Items.Armors.Armour import Armour


class NoArmour(Armour):
    def __init__(self):
        super().__init__(0, 0)
        self._description = "You are wearing no armour.\n"

    def get_id(self):
        return 311