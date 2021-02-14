from Items.Armors.Armour import Armour


class TemArmor(Armour):
    def __init__(self):
        super().__init__(0, 100)
        self._description = "Strongest defensive option early game.\n"

    def get_id(self):
        return 302