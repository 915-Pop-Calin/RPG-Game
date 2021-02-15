from Items.Armors.Armour import Armour


class Cloth(Armour):
    def __init__(self):
        super().__init__(0, 10)
        self._description = "Strong armour early on.\n"

    def get_id(self):
        return 301